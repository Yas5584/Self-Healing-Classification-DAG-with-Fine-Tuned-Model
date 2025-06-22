import json
from datetime import datetime
import os

LOG_FILE = "execution.log"

def log_event(event_type, data):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "data": data
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

def parse_logs():
    if not os.path.exists(LOG_FILE):
        return []
    
    with open(LOG_FILE, "r") as f:
        return [json.loads(line) for line in f.readlines()]