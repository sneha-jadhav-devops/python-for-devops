import docker

client = docker.from_env()

container_name = "nginx"

container = client.containers.get(container_name)

# Start container
container.start()
print("Container started")

# Stop container
# container.stop()
# print("Container stopped")
