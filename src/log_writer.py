import os
import datetime


class Log_writer:
    """
    Handles the logging.
    """
    def __init__(self):
        """
        Initialize the connection
        """
        self.log_file = 'log.txt'
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as log:
                log.write("Log file created.\n")

    def log(self, message):
        """
        Writes the log.
        """
        with open(self.log_file, 'a') as log:
            timestamp = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
            log.write(f"{timestamp}: {message}\n")

    def clear_log(self):
        """
        Clears the log.
        """
        open(self.log_file, 'w').close()
