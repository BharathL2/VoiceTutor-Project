# Memory agent for tracking sessions
import json

MEMORY_FILE = "memory.json"

def save_session(entry):
    try:
        with open(MEMORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

    history.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_history():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []
