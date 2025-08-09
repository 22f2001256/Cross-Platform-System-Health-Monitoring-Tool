import os
import json
import time
from client import collect_data, send_data

INTERVAL_MINUTES = 1
STATE_FILE = "state.json"

def load_last_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    
    return None


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

def state_changed(old, new):
    return old != new

def run_daemon():
    print("Starting daemon... checking every {INTERVAL_MINUTES} minutes")

    while(True):
        current_state = collect_data()
        last_state = load_last_state()

        if(state_changed(current_state, last_state)):
            print("Change detected")
            status, response = send_data(current_state)
            print("Server Response:", status, response)
            
            if status and status == 200:
                save_state(current_state)

        else:
            print("No change detected")

        time.sleep(INTERVAL_MINUTES*60)


if __name__ == "__main__":
    run_daemon()