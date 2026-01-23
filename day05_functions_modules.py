# DAY 5 – FUNCTIONS & MODULES 

import os
import time
import platform

# -------------------------------
# Simple Function
# -------------------------------
def show_message():
    print("Starting DevOps automation script")

show_message()

# -------------------------------
# Function with Parameter
# -------------------------------
def check_service(service_name):
    print(service_name, "service is running")

check_service("nginx")
check_service("docker")

# -------------------------------
# Function with Return Value
# -------------------------------
def get_default_port():
    return 80

port = get_default_port()
print("Default port:", port)

# -------------------------------
# Function with Default Argument
# -------------------------------
def deploy_app(environment="dev"):
    print("Deploying application to", environment)

deploy_app()
deploy_app("production")

# -------------------------------
# Function with Condition
# -------------------------------
def service_health(status):
    if status == "running":
        return "Service is healthy"
    else:
        return "Service needs attention"

print(service_health("running"))
print(service_health("stopped"))

# -------------------------------
# Using os Module
# -------------------------------
print("Current working directory:", os.getcwd())
print("User home directory:", os.path.expanduser("~"))

# Environment variable example
env = os.getenv("ENVIRONMENT", "development")
print("Deployment environment:", env)

# -------------------------------
# Using time Module
# -------------------------------
print("Waiting for service to start...")
time.sleep(2)
print("Service check complete")

# -------------------------------
# Using platform Module
# -------------------------------
print("Operating System:", platform.system())
print("OS Version:", platform.release())

# -------------------------------
# Real DevOps Style Example
# -------------------------------
def restart_service(service_name, retries=3):
    attempt = 1
    while attempt <= retries:
        print("Restarting", service_name, "- Attempt", attempt)
        time.sleep(1)
        attempt += 1
    print(service_name, "restart completed")

restart_service("nginx")
