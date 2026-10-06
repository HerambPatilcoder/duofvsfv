from pathlib import Path
import sys
import psutil

report = Path("process_report.txt")

if len(sys.argv) < 2:
    print("Please provide a process name.")
    sys.exit(1)

process = sys.argv[1]

with report.open("w") as f:
    f.write("PROCESS INFORMATION REPORT\n")
    f.write("--------------------------\n")

    found = False

    for proc in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            name = proc.info["name"] or ""

            if process.lower() in name.lower():

                if not found:
                    f.write(f"Process: {process}\n")
                    f.write("PID     CPU%    MEM%\n")

                f.write(
                    f"{proc.info['pid']:<8}"
                    f"{proc.info['cpu_percent']:<8.1f}"
                    f"{proc.info['memory_percent']:.1f}\n"
                )

                found = True

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found:
        f.write(f"Process '{process}' is not running.\n")

print(f"Report saved to {report}")