# Importing the required libraries
from plyer import notification as np  # Importing the notification module
import time

# Main program loop
if __name__ == '__main__':
    while True:
        np.notify(
            title="Keep Doing",  # Title of the notification
            message="If you want to shine like a sun, first burn like a sun.",  # Notification message
            timeout=30  # Timeout (in seconds) for how long the notification should be visible
        )
        time.sleep(3600)  # Wait for 1 hour before sending the next notification

