import subprocess
import time

services = ["nginx", "docker"]

while True:
    for service in services:
        status = subprocess.getoutput(f"systemctl is-active {service}")
        print(service, ":", status)
    print("-" * 40)
    time.sleep(10)
