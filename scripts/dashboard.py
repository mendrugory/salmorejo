import threading
from queue import deque

import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly
import plotly.graph_objs as go

MAX = 13
MAX_PODS = 20

X = deque(maxlen = MAX)
X.append(1)

PODS = deque(maxlen = MAX)
PODS.append(0)

LOG = deque(maxlen = MAX)

counters = dict()


def callback(event):
    global counters

    if event['raw_object']['metadata']['namespace'] != "default":
        return

    name = event['raw_object']['metadata']['name']
    kind = event['raw_object']['kind']
    t = event['type']

    current_count = counters.get(kind, 0)
    if t == 'ADDED':
        counters[kind] = current_count + 1
        
    if t == 'DELETED':
        counters[kind] = max(current_count - 1, 0)

    LOG.append(f"{kind} {name} has been {t}")


# layouts

def log_layout():
    return html.Div(
        className="border",
        style={
            'padding': '50px',
            'height': '600px',
        },
        children=[
            html.H2(children='Log', style={"text-align": "center"}),
            html.Div(
                id='live-log',
                className="border",
                style={
                    'whiteSpace': 'pre-line',
                    'text-align': 'left',
                    'background-color': bg_graph_color,
                    'color': text_color,
                    'padding': '50px',
                    'font-size': '20px',
                    'height': '450px',
                }
            ),
            dcc.Interval(
                id = 'log-update',
                interval = 1000,
                n_intervals = 0
            )
        ]
    )

def gauge_layout():
    return html.Div(
        className="border",
        style={
            'padding': '50px',
            'height': '600px',
        },
        children=[
            html.H2(children='State', style={"text-align": "center"}),
            dcc.Graph(id = 'live-gauge', animate = True),
            dcc.Interval(
                id = 'gauge-update',
                interval = 1000,
                n_intervals = 0
            )
        ]
    )

def scatter_layout():
    return html.Div(
        className="border",
        style={
            'padding': '50px',
        },
        children=[
            html.H2(children='History', style={"text-align": "center"}),
            dcc.Graph(id = 'live-graph', animate = True),
            dcc.Interval(
                id = 'graph-update',
                interval = 1000,
                n_intervals = 0
            )
        ]
    )

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

bg_color = '#262A2F'
bg_graph_color = '#32383E'
text_color = 'white'
line_color = 'red'

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1(
                    children='Pods Dashboard', 
                    style={
                        "text-align": "center",
                        'padding': '50px',
                    }
                )
            )
        ),
        dbc.Row(
            dbc.Col(
                scatter_layout()
            )
        ),
        dbc.Row(
            [
                dbc.Col(gauge_layout()),
                dbc.Col(log_layout())
            ]
        ),    
    ],
    fluid=True,
    style={
        'background-color': bg_color,
        'color': text_color,
        'padding': '10px',
    }
)


# callbacks

@app.callback(
    Output('live-graph', 'figure'),
    [ Input('graph-update', 'n_intervals') ]
)
def update_graph(n):
    global counters

    X.append(X[-1]+1)
    PODS.append(counters.get("Pod", 0))

    pods = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(PODS),
            name='Pods',
            mode='lines+markers'
    )


    return {
            'data': [pods],
            'layout' : go.Layout(
                xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [0,max(PODS) + 2]),
            )}


@app.callback(
    Output('live-gauge', 'figure'),
    [ Input('gauge-update', 'n_intervals') ]
)
def update_gauge(n):
    gauge = plotly.graph_objs.Indicator(
            value=PODS[-1],
            name='Pods',
            mode='gauge+number',
            gauge={
                'bar': {'color': text_color},
                'bordercolor': text_color,
                'bgcolor': bg_graph_color,
                'axis': {'range': [0, MAX_PODS], 'tickcolor': '#39405F'},
            }
    )

    return {
                'data': [gauge],
                'layout' : go.Layout(
                    xaxis=dict(range=[0, MAX_PODS]),
                )
            }


@app.callback(
    Output('live-log', 'children'),
    [ Input('log-update', 'n_intervals') ]
)
def update_log(n):
    return "\n".join([str(l) for l in list(LOG)])


# Web server
threading.Thread(target=app.run_server).start()
