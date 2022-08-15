from beautifultable import BeautifulTable

table = BeautifulTable()
table.columns.header = ["KIND", "NAMESPACE", "NAME", "PHASE"]

def callback(event):
    phase = event['raw_object']['status'].get('phase') if 'phase' in event['raw_object']['status'] else ""
    table.rows.append([
        event['raw_object']['kind'],
        event['raw_object']['metadata']['namespace'],
        event['raw_object']['metadata']['name'],
        phase
    ])
    print("\n*****\n")
    print(table)
