import logging
import time

logging.basicConfig(
    filename="service.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_service(service):
    logging.info(f"Checking {service}")
    time.sleep(1)
    logging.info(f"{service} is running")

services = ["nginx", "docker", "jenkins"]

for service in services:
    check_service(service)
