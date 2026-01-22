# DAY 4 – CONDITIONALS & LOOPS (DEVOPS FOCUSED)

# -------------------------------
# Conditional Statements

service_status = "running"
environment = "production"

if service_status == "running":
    print("Service is running")
else:
    print("Service is not running")

# -------------------------------
# Comparison & Logical Operators
# -------------------------------
cpu_usage = 78

if cpu_usage > 75:
    print("High CPU usage alert")

monitoring_enabled = True

if cpu_usage > 75 and monitoring_enabled:
    print("Alert sent to monitoring system")

# -------------------------------
# for Loop (Server Inventory)
# -------------------------------
servers = ["web1", "web2", "db1", "cache1"]

for server in servers:
    print("Checking server:", server)

# -------------------------------
# for Loop with Condition
# -------------------------------
for server in servers:
    if server.startswith("db"):
        print("Database server found:", server)

# -------------------------------
# while Loop (Retry Mechanism)
# -------------------------------
retry_count = 0
max_retries = 3

while retry_count < max_retries:
    print("Checking service... Attempt:", retry_count + 1)
    retry_count += 1

# -------------------------------
# break Example
# -------------------------------
for server in servers:
    if server == "db1":
        print("Critical server found. Stopping loop.")
        break

# -------------------------------
# continue Example
# -------------------------------
for server in servers:
    if server == "cache1":
        print("Skipping cache server")
        continue
    print("Processing server:", server)

# -------------------------------
# Real DevOps Style Example
# -------------------------------
services = [
    {"name": "nginx", "status": "running"},
    {"name": "redis", "status": "stopped"},
    {"name": "postgres", "status": "running"}
]

for service in services:
    if service["status"] == "running":
        print(service["name"], "is healthy")
    else:
        print(service["name"], "needs attention")
