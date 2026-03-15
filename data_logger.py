import csv
from datetime import datetime

LOG_FILE = "ball_log.csv"

def log_ball_position(x, y):
    """
    Append the ball's x, y position with timestamp to CSV.
    """
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        writer.writerow([timestamp, x, y])
