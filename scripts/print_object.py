import json

def callback(event):
    print(f"\n---------- {event['raw_object']['kind']} -------------")
    print(json.dumps(event['raw_object'], sort_keys=True, indent=4))
    print("--------------------------------------\n")