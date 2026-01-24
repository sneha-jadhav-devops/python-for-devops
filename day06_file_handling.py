# DAY 6 – FILE HANDLING & LOGS (DEVOPS FOCUSED)

import os
from datetime import datetime

log_file = "deployment.log"

# -------------------------------
# Writing Initial Log
# -------------------------------
with open(log_file, "w") as file:
    file.write("Deployment started\n")

# -------------------------------
# Appending Logs
# -------------------------------
with open(log_file, "a") as file:
    file.write("nginx service started\n")
    file.write("docker service running\n")

# -------------------------------
# Adding Timestamped Logs
# -------------------------------
with open(log_file, "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Health check passed\n")

# -------------------------------
# Reading Logs
# -------------------------------
print("Reading deployment logs:")
with open(log_file, "r") as file:
    for line in file:
        print(line.strip())

# -------------------------------
# Checking File Existence
# -------------------------------
if os.path.exists(log_file):
    print("Log file exists")
else:
    print("Log file not found")
