import os
import threading
from beautifultable import BeautifulTable

counters = dict()
mutex = threading.Lock()

_separator = "***"

def callback(event):
    global counters
    global mutex
    namespaced_name = f"{event['raw_object']['metadata']['namespace']}{_separator}{event['raw_object']['kind']}"
    mutex.acquire()
    current_count = counters.get(namespaced_name, 0)
    if event['type'] == 'ADDED':
        counters[namespaced_name] = current_count + 1
    if event['type'] == 'DELETED':
        counters[namespaced_name] = max(current_count - 1, 0)
    print_counters()
    mutex.release()
    

def print_counters():
    global counters
    table = BeautifulTable()
    table.columns.header = ["KIND", "NAMESPACE", "COUNT"]
    for key, count in counters.items():
        namespace, kind = key.split(_separator)
        table.rows.append([kind, namespace, count])
    os.system("clear")
    print(table)
