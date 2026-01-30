import docker

client = docker.from_env()

container_name = "nginx"

container = client.containers.get(container_name)

if container.status == "running":
    print(container_name, "is healthy")
else:
    print(container_name, "is not running")
