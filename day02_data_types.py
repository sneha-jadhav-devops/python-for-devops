"""
DAY 2 – PYTHON DATA TYPES FOR DEVOPS

Topics covered:
- Strings
- Integers
- Lists
- Dictionaries
- Real DevOps examples
"""


# STRING DATA TYPE

service_name = "nginx"
environment = "production"

print("Service Name:", service_name)
print("Environment:", environment)


# INTEGER DATA TYPE

port = 80
replicas = 3

print("Service Port:", port)
print("Number of Replicas:", replicas)


# LIST DATA TYPE
# Used to store multiple servers

servers = ["web-server-1", "web-server-2", "db-server-1"]

print("Servers List:", servers)
print("First Server:", servers[0])

# Adding a new server
servers.append("cache-server-1")
print("Updated Servers List:", servers)


# DICTIONARY DATA TYPE
# Used to store service configuration

service_config = {
    "name": "nginx",
    "port": 80,
    "status": "running",
    "environment": "production"
}

print("Service Configuration:", service_config)
print("Service Name:", service_config["name"])
print("Service Status:", service_config["status"])

# Updating dictionary value
service_config["status"] = "stopped"
print("Updated Service Status:", service_config["status"])


# DEVOPS STYLE OUTPUT

print(
    f"Service {service_config['name']} "
    f"is running on port {service_config['port']} "
    f"in {service_config['environment']} environment"
)
