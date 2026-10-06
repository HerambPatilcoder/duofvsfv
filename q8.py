from pathlib import Path
from datetime import datetime
import sys
import psutil


REPORT = Path("heramb_report.txt")


def get_current_users():
    """Get currently logged-in users."""
    users = []

    for entry in psutil.users():
        users.append(
            (
                entry.name,
                entry.terminal,
                datetime.fromtimestamp(entry.started)
            )
        )

    return users


def generate_report(user=None):

    current = get_current_users()

    with REPORT.open("w") as f:

        f.write("USER LOGIN REPORT\n")
        f.write("-----------------\n\n")

        # Currently logged-in users
        f.write("Currently Logged-in Users:\n")

        for username, terminal, login_time in current:
            f.write(
                f"{username:<15} "
                f"{terminal or '-':<10} "
                f"{login_time}\n"
            )

        # Login time
        f.write("\nLogin Time of Each User:\n")

        for username, terminal, login_time in current:
            f.write(
                f"{username:<15} "
                f"{login_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            )

        # Number of logged-in users
        f.write(
            f"\nNumber of Logged-in Users: "
            f"{len(current)}\n"
        )

        # Check specified user
        f.write("\n")

        if user:
            logged_users = {
                username
                for username, _, _ in current
            }

            if user in logged_users:
                f.write(
                    f"{user} is currently logged in.\n"
                )
            else:
                f.write(
                    f"{user} is not currently logged in.\n"
                )
        else:
            f.write("No user specified.\n")

        # Historical login information
        f.write("\nLast 10 User Logins:\n")
        f.write(
            "Historical login information is "
            "OS-specific and is not available through "
            "Python's standard cross-platform interface.\n"
        )

        f.write(
            "\nNumber of Unique Users Who Logged In: "
            "Not available\n"
        )

        f.write("\nMost Recent Logins:\n")
        f.write(
            "Historical login information is "
            "OS-specific.\n"
        )


# Command-line argument
user = sys.argv[1] if len(sys.argv) > 1 else None

generate_report(user)

print(f"\nReport saved to {REPORT}")