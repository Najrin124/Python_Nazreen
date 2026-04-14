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

# 5
# import os, time

# threshold = time.time() - (30 * 86400)

# for root, _, files in os.walk("/home/mistu/Documents/Azahar/0_Cloud/"):
#     for f in files:
#         fp = os.path.join(root, f)
#         if os.path.getmtime(fp) < threshold:
#             os.remove(fp)

# 6
import os, shutil

for f in os.listdir("/home/mistu/Documents/Azahar/0_Cloud/Python3"):
    if os.path.isfile(f):
        ext = f.split('.')[-1]
        os.makedirs(ext, exist_ok=True)
        shutil.move(f, os.path.join(ext, f))