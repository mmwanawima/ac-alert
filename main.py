import time
import logging
from monitor import get_power_status

# Setup logger to write to the file
logging.basicConfig(
    filename='power_events.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    last_state = get_power_status()
    print(f"Monitoring started. Current state: {'AC' if last_state else 'Battery'}")
    
    while True:
        current_state = get_power_status()
        
        # Only log if the state has changed
        if current_state != last_state:
            status = "AC Power Connected" if current_state else "AC Power Disconnected"
            logging.info(f"Power change detected: {status}")
            print(f"Logged: {status}")
            last_state = current_state
            
        time.sleep(10)

if __name__ == "__main__":
    main()