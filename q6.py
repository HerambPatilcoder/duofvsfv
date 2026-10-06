from pathlib import Path
from datetime import datetime
import getpass
import socket
import shutil
import psutil


report = Path("heramb.txt")

with report.open("w") as f:
    f.write("SYSTEM INFORMATION REPORT\n")
    f.write(f"Date and Time: {datetime.now()}\n")
    f.write(f"Logged-in User: {getpass.getuser()}\n")
    f.write(f"Hostname: {socket.gethostname()}\n")
    f.write(f"Current Working Directory: {Path.cwd()}\n")

    # Disk space
    total, used, free = shutil.disk_usage(Path.home())

    f.write("Available Disk Space:\n")
    f.write(f"Total: {total / (1024**3):.2f} GB\n")
    f.write(f"Used: {used / (1024**3):.2f} GB\n")
    f.write(f"Free: {free / (1024**3):.2f} GB\n")

    # Memory
    memory = psutil.virtual_memory()

    f.write("Available Memory:\n")
    f.write(f"Total: {memory.total / (1024**3):.2f} GB\n")
    f.write(f"Available: {memory.available / (1024**3):.2f} GB\n")

    # Uptime
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())

    days = uptime.days
    hours = uptime.seconds // 3600
    minutes = (uptime.seconds % 3600) // 60

    f.write(
        f"System Uptime: {days} days, "
        f"{hours} hours, {minutes} minutes\n"
    )

print(f"Report saved to {report}")