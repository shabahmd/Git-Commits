import subprocess
import random
from datetime import datetime, timedelta

def generate_commit_message():
    messages = [
        "Fixed a bug",
        "Added a new feature",
        "Refactored code",
        "Updated documentation",
        "Improved performance",
    ]
    return random.choice(messages)
    
def generate_commit_date(base_date, days_offset):
    offset = timedelta(days=days_offset)
    return base_date + offset


def create_commits(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        commit_message = generate_commit_message()
        subprocess.run(["git", "commit", "--date", current_date.strftime("%Y-%m-%d %H:%M:%S"), "-m", commit_message])
        current_date += timedelta(days=1)
if __name__ == "__main__":
    base_date = datetime(2023, 1, 1)  # Adjust the start date as needed
    end_date = datetime(2023, 12, 31)  # Adjust the end date as needed
    create_commits(base_date, end_date)
