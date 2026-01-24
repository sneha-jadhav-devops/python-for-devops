# DAY 6 – EXTRA: ADVANCED FILE HANDLING & LOG ANALYSIS (DEVOPS)

import os
from datetime import datetime

# -------------------------------
# Create logs directory
# -------------------------------
log_dir = "logs"

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_file = os.path.join(log_dir, "deployment.log")

# -------------------------------
# Write initial log
# -------------------------------
with open(log_file, "w") as file:
    file.write("[INFO] Deployment started\n")

# -------------------------------
# Append logs with levels
# -------------------------------
with open(log_file, "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] [INFO] nginx service started\n")
    file.write(f"[{timestamp}] [WARNING] Disk usage above 80%\n")
    file.write(f"[{timestamp}] [ERROR] Service restart failed\n")

# -------------------------------
# Read full log file
# -------------------------------
print("\n--- Full Logs ---")
with open(log_file, "r") as file:
    for line in file:
        print(line.strip())

# -------------------------------
# Filter ERROR logs (log analysis)
# -------------------------------
print("\n--- ERROR Logs ---")
with open(log_file, "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())

# -------------------------------
# Safe file read with error handling
# -------------------------------
try:
    with open("missing.log", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("\nLog file not found, skipping safely")
