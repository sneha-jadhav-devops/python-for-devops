import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

print("System Uptime:")
print(run_command("uptime"))

print("Disk Usage:")
print(run_command("df -h"))

print("Memory Usage:")
print(run_command("free -m"))
