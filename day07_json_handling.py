# DAY 7 – JSON HANDLING 

import json

# Read JSON file
with open("day07_sample.json", "r") as file:
    config = json.load(file)

print("Service Name:", config["service"])
print("Port:", config["port"])
print("Environment:", config["environment"])

# Write JSON file
service_status = {
    "service": "docker",
    "status": "running",
    "port": 2375
}

with open("service_status.json", "w") as file:
    json.dump(service_status, file, indent=4)

print("Service status JSON created")
