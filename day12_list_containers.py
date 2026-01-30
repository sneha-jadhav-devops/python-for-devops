import docker

client = docker.from_env()

containers = client.containers.list(all=True)

print("Docker Containers:")
for container in containers:
    print(container.name, "-", container.status)
