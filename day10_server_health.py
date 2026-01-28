import subprocess
import logging
import time

logging.basicConfig(
    filename="server_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check(command, title):
    logging.info(f"Checking {title}")
    output = subprocess.getoutput(command)
    print(f"\n{title}:\n{output}")

check("uptime", "System Uptime")
check("df -h", "Disk Usage")
check("free -m", "Memory Usage")

logging.info("Server health check completed")
