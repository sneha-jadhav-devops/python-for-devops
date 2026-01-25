# DAY 7 – YAML HANDLING (DEVOPS FOCUSED)

import yaml

with open("day07_config.yaml", "r") as file:
    config = yaml.safe_load(file)

print("Service Name:", config["service"]["name"])
print("Port:", config["service"]["port"])
print("Replicas:", config["service"]["replicas"])
print("Environment:", config["environment"])
