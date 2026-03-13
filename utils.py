import os
import re
from datetime import datetime

def get_current_timestamp():
    return int(datetime.now().timestamp())

def is_valid_email(email):
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def get_environment_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        return None

def parse_json_data(json_string):
    try:
        import json
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        timestamp = get_current_timestamp()
        log_message = f"{timestamp} - {message}"
        write_to_file(self.log_file, log_message + "\n")

    def error(self, message):
        self.log(f"ERROR: {message}")

    def info(self, message):
        self.log(f"INFO: {message}")