import subprocess

service = "nginx"

result = subprocess.run(
    f"systemctl is-active {service}",
    shell=True,
    capture_output=True,
    text=True
)

if result.stdout.strip() == "active":
    print(service, "service is running")
else:
    print(service, "service is NOT running")
