import time
import os
from alerter import send_security_alert

# This is the standard file where Ubuntu stores login information
LOG_FILE = "/var/log/auth.log"

def monitor_logs():
    print("[*] Monitoring started... Watching for failed logins.")
    
    # Open the file and go to the very end so we only see NEW logs
    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)  # Wait for a new line to be written
                continue
            
            # Look for the "Failed password" keyword
            if "Failed password" in line:
                print(f"[!] SECURITY EVENT DETECTED: {line.strip()}")
                send_security_alert("Brute Force Attempt", line)

if __name__ == "__main__":
    monitor_logs()