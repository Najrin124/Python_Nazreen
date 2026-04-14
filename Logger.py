import os
from datetime import datetime


def writelog(message):

    # current working directory
    app_path = os.getcwd()

    # logs folder path 
    log_dir_path = os.path.join(app_path, "logs")

    # create logs folder if not exists
    os.makedirs(log_dir_path, exist_ok=True)

    # safe timestamp for filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # log file path
    new_log_file_name = os.path.join(log_dir_path, f"app_{timestamp}.log")

    # log line
    log_line = f"{timestamp} {message}\n"

    with open(new_log_file_name, "a") as f:
        f.write(log_line)

    print(log_line.strip())



writelog("Server started")
writelog("User logged in")
writelog("Database error")

####################################################


def find_log_files():
    app_path = os.getcwd()
    log_dir = os.path.join(app_path, "logs")

    log_files = []

    if not os.path.exists(log_dir):
        print("logs directory does not exist")
        return log_files

    for file in os.listdir(log_dir):

        if file.endswith(".log"):
            full_path = os.path.join(log_dir, file)
            log_files.append(full_path)

    return log_files


logs = find_log_files()
for log in logs:
    print(f"Found: {log}")


###################################################

import time

def delete_old_logs(days=5):

    app_path = os.getcwd()
    log_dir = os.path.join(app_path, "logs")

    if not os.path.exists(log_dir):
        print("logs directory does not exist")
        return

    current_time = time.time()

    for file in os.listdir(log_dir):

        if file.endswith(".log"):

            full_path = os.path.join(log_dir, file)

            file_modified_time = os.path.getmtime(full_path)

            file_age = current_time - file_modified_time
            
            DELETE_AFTER_SECONDS = 2   # 2-sec old files for testing
            
            # DELETE_AFTER_SECONDS = min * 60 (sec)
            # DELETE_AFTER_SECONDS = hour * 60 * 60 (sec)
            # DELETE_AFTER_SECONDS = days * 24 * 60 * 60 (sec)

            if file_age > DELETE_AFTER_SECONDS:
                if os.path.exists(full_path):
                    os.remove(full_path)
                    print("Deleted:", full_path)

time.sleep(30)   # wait 30 seconds
delete_old_logs()