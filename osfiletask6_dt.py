# import os
# 1
# for root, dirs, files in os.walk("/home/mistu/Documents/Azahar/0_Cloud/Python3"):
#     for file in files:
#         print(os.path.join(root, file))


# 2
# import os

# max_size = 0
# largest_file = ""

# for root, _, files in os.walk("/home/mistu/Documents/Azahar/0_Cloud/Python3"):
#     for f in files:
#         fp = os.path.join(root, f)
#         size = os.path.getsize(fp)
#         if size > max_size:
#             max_size = size
#             largest_file = fp

# print(largest_file, max_size)


# 3
# import os

# total = 0
# for root, _, files in os.walk("/home/mistu/Documents/Azahar/0_Cloud/Python3"):
#     for f in files:
#         total += os.path.getsize(os.path.join(root, f))

# print(total)
# 4
# import os, hashlib

# hash_map = {}

# def file_hash(path):
#     h = hashlib.md5()
#     with open(path, 'rb') as f:
#         h.update(f.read())
#     return h.hexdigest()

# for root, _, files in os.walk("pa/home/mistu/Documents/Azahar/0_Cloud/Python3"):
#     for f in files:
#         fp = os.path.join(root, f)
#         h = file_hash(fp)
#         hash_map.setdefault(h, []).append(fp)

# duplicates = [v for v in hash_map.values() if len(v) > 1]
# print(duplicates)

# # 5
# import os, time

# threshold = time.time() - (30 * 86400)

# for root, _, files in os.walk("/home/mistu/Documents/Azahar/0_Cloud/Python3"):
#     for f in files:
#         fp = os.path.join(root, f)
#         if os.path.getmtime(fp) < threshold:
#             os.remove(fp)

# 6
# import os, shutil

# for f in os.listdir("/home/mistu/Documents/Azahar/0_Cloud/Python3"):
#     if os.path.isfile(f):
#         ext = f.split('.')[-1]
#         os.makedirs(ext, exist_ok=True)
#         shutil.move(f, os.path.join(ext, f))


# 7
# import os

# for i, f in enumerate(os.listdir("/home/mistu/Documents/Azahar/0_Cloud/Python3")):
#     new_name = f"file_{i}.txt"
#     os.rename(os.path.join("/home/mistu/Documents/Azahar/0_Cloud/Python3", f),
#               os.path.join("/home/mistu/Documents/Azahar/0_Cloud/Python3ss", new_name))

# 10
# import os, time

# seen = set(os.listdir("/home/mistu/Documents/Azahar/0_Cloud/Python3"))

# while True:
#     time.sleep(2)
#     current = set(os.listdir("/home/mistu/Documents/Azahar/0_Cloud/Python3"))
#     new_files = current - seen
#     if new_files:
#         print("New files:", new_files)
#     seen = current


# import os

# def find(path, name):
#     for root, _, files in os.walk("/home/mistu/Documents/Azahar/0_Cloud/Python3"):
#         for f in files:
#             if name in f:
#                 print(os.path.join(root, f))

# find("/home/mistu/Documents/Azahar/0_Cloud/Python3", "test")

# 13
# import os, argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--name")
# parser.add_argument("--min_size", type = int)
# args = parser.parse_args()
# for root, _, files in os.walk("."):
#     for f in files:
#         fp = os.path.join(root, f)
#         if args.name and args.name not in f:
#             continue
#         if args.min_size and os.path.getsize(fp) <args.min_size:
#             continue
#         print(fp)

# 14. Handle permission errors during file operations
# import os
# try:
#     os.remove("/home/mistu/Documents/Azahar/0_Cloud/Python3/file.txt")
# except PermissionError:
#     print("Permission denied")
# except FileNotFoundError:
#     print("File not found")

# 15
# import os 
# for root, dirs, files in os.walk("/home/mistu/Documents/Azahar/0_Cloud/Python3", followlinks=False):
#   print(root)  

# 16
# import os
# p = ""
# if os.path.isfile(p):
#     print("File")
# elif os.path.isdir(p):
#     print("Directory")
# elif os.path.islink:
#     print("Symlink")

# 17
# from pathlib import Path
# p = Path("/home/mistu/Documents/Azahar/0_Cloud/Python3")
# print(p.resolve())