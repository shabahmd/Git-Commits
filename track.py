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
