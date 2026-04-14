# Log Cleanup Script
import os 
# from datetime import datetime 

# def writelog(messages):
#     app_path = os.getcwd()
#     log_dir_path = os.path.join(app_path, "logs")
#     os.makedirs(log_dir_path, exist_ok=True)
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     new_log_file_name = os.path.join(log_dir_path,)



import os

def get_size(folder):
    total = 0
    for root, _, files in os.walk(folder):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return total

size = get_size("/path")
print(f"Total disk usage: {size / (1024**3):.2f} GB")