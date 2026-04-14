
# 1.You are given a 10GB log file. Build a system to fetch the last 100 lines instantly.
# def get_last_n_lines(file_path, n=100):
#     with open(file_path, "rb") as f:
#         f.seek(0, 2)  # move to end of file
#         file_size = f.tell()
        
#         buffer = bytearray()
#         pointer = file_size - 1
#         lines = []

#         while pointer >= 0 and len(lines) < n:
#             f.seek(pointer)
#             byte = f.read(1)
            
#             if byte == b'\n':
#                 lines.append(buffer.decode()[::-1])
#                 buffer = bytearray()
#             else:
#                 buffer.extend(byte)
            
#             pointer -= 1

#         if buffer:
#             lines.append(buffer.decode()[::-1])

#     return lines[::-1]


# # Usage
# last_lines = get_last_n_lines("log.txt", 100)

# for line in last_lines:
#     print(line)

# 2.A log file is continuously growing. Design a system to read new lines in real time. given code python each line explain
# import time

# def follow(file_path):
#     with open(file_path, "r") as file:
#         file.seek(0, 2)  # Move to end of file

#         while True:
#             line = file.readline()

#             if not line:
#                 time.sleep(0.5)
#                 continue

#             yield line


# if __name__ == "__main__":
#     for line in follow("log.txt"):
#         print(line.strip())


# 3.Remove Duplicates from a Huge File
# import heapq
# import tempfile
# import os

# CHUNK_SIZE = 100000

# def split_file(input_file):
#     temp_files = []
    
#     with open(input_file, 'r') as f:
#         while True:
#             lines = []
            
#             for _ in range(CHUNK_SIZE):
#                 line = f.readline()
#                 if not line:
#                     break
#                 lines.append(line.strip())

#             if not lines:
#                 break

#             lines = sorted(set(lines))  # remove duplicates + sort
            
#             temp = tempfile.NamedTemporaryFile(delete=False, mode='w')
#             temp.write("\n".join(lines) + "\n")
#             temp.close()
            
#             temp_files.append(temp.name)

#     return temp_files





# Two large sorted files need to be merged into a third sorted file efficiently.
# def merge_sorted_files(file1, file2, output):
#     with open(file1) as f1, open(file2) as f2, open(output, 'w') as out:
#         line1 = f1.readline()
#         line2 = f2.readline()

#         while line1 and line2:
#             if line1 <= line2:
#                 out.write(line1)
#                 line1 = f1.readline()
#             else:
#                 out.write(line2)
#                 line2 = f2.readline()

#         while line1:
#             out.write(line1)
#             line1 = f1.readline()

#         while line2:
#             out.write(line2)
#             line2 = f2.readline()

# merge_sorted_files("/home/mistu/Documents/Azahar/0_Cloud/Python3/file1.txt", 
#                    "/home/mistu/Documents/Azahar/0_Cloud/Python3/file2.txt", 
#                    "/home/mistu/Documents/Azahar/0_Cloud/Python3/output.txt")


# 5.Extract Only ERROR Logs
# def extract_errors(input_file, output_file):
#     with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
#         for line in infile:
#             if "ERROR" in line:
#                 outfile.write(line)

# extract_errors("/home/mistu/Documents/Azahar/0_Cloud/Python3/input.txt", "/home/mistu/Documents/Azahar/0_Cloud/Python3/out.txt")

#6. 

# def count_unique_ips(file_path):
#     unique_ips = set()

#     with open(file_path, 'r') as f:
#         for line in f:
#             ip = line.strip()
#             unique_ips.add(ip)

#     return len(unique_ips)
# count_unique_ips("/home/mistu/Documents/Azahar/0_Cloud/Python3/count.txt")

# 7
# from collections import Counter


# def top_n_words(file_path, n=10, max_words=None):
#     """Return the top-n most frequent words in a file.
#     If max_words is provided, count only the first max_words words."""
#     freq = Counter()
#     seen = 0

#     with open(file_path, 'r') as f:
#         for line in f:
#             for word in line.strip().split():
#                 if max_words is not None and seen >= max_words:
#                     return freq.most_common(n)
#                 freq[word] += 1
#                 seen += 1

#     return freq.most_common(n)


# def compare_top_n_words(file1, file2, n=10, max_words=10):
#     """Compare top-n words from the first max_words words of two files."""
#     top1 = top_n_words(file1, n=n, max_words=max_words)
#     top2 = top_n_words(file2, n=n, max_words=max_words)

#     set1 = {word for word, _ in top1}
#     set2 = {word for word, _ in top2}

#     return {
#         'top1': top1,
#         'top2': top2,
#         'only_in_file1': sorted(set1 - set2),
#         'only_in_file2': sorted(set2 - set1),
#         'common': sorted(set1 & set2),
#     }


# if __name__ == '__main__':
#     file_a = 'words.txt'
#     file_b = 'file2.txt'

#     print('Top 10 words in the first 10 words of', file_a)
#     print(top_n_words(file_a, max_words=10))

#     print('\nTop 10 words in the first 10 words of', file_b)
#     print(top_n_words(file_b, max_words=10))

#     print('\nComparison:')
#     diff = compare_top_n_words(file_a, file_b, max_words=10)
#     print(diff)

# 8

# def compare_files(file1, file2):
#     with open(file1) as f1, open(file2) as f2:
#         line_num = 1

#         while True:
#             line1 = f1.readline()
#             line2 = f2.readline()

#             if not line1 and not line2:
#                 break

#             if line1 != line2:
#                 print(f"Difference at line {line_num}")

#             line_num += 1
# compare_files("/home/mistu/Documents/Azahar/0_Cloud/Python3/largest.txt","/home/mistu/Documents/Azahar/0_Cloud/Python3/small.txt")        



#9. A CSV file is 5GB. Convert it to JSON without memory overflow.
# import csv
# import json

# def csv_to_json_streaming(csv_file, json_file):
#     with open(csv_file, 'r', newline='', encoding='utf-8') as cf, \
#          open(json_file, 'w', encoding='utf-8') as jf:
        
#         reader = csv.DictReader(cf)

#         jf.write("[\n")
#         first = True

#         for row in reader:
#             if not first:
#                 jf.write(",\n")
#             json.dump(row, jf)
#             first = False

#         jf.write("\n]")     

# 10.A file may contain mixed encoding. Build a system to safely read it.
# def safe_read(file_path):
#     try:
#         # First try UTF-8
#         with open(file_path, 'r', encoding='utf-8') as f:
#             for line in f:
#                 process(line)
#     except UnicodeDecodeError:
#         # Fallback encoding
#         with open(file_path, 'r', encoding='latin-1', errors='replace') as f:
#             for line in f:
#                 process(line)

# def process(line):
#     print(line.strip())


# if __name__ == "__main__":
#     file_path = "test.txt"   # change to your file name
#     safe_read("test.txt")

# 12
# import os

# def merge_chunks(output_file, chunk_prefix="chunk_", extension=".part"):
#     # Get all chunk files in correct order
#     chunk_files = sorted(
#         [f for f in os.listdir() if f.startswith(chunk_prefix) and f.endswith(extension)],
#         key=lambda x: int(x.replace(chunk_prefix, "").replace(extension, ""))
#     )

#     with open(output_file, 'wb') as outfile:
#         for chunk_file in chunk_files:
#             print(f"Merging {chunk_file}...")
#             with open(chunk_file, 'rb') as infile:
#                 while True:
#                     data = infile.read(1024 * 1024)  # Read 1MB at a time
#                     if not data:
#                         break
#                     outfile.write(data)

#     print("Merging completed!")
#     print(os.path.getsize("largefile.dat"))


# if __name__ == "__main__":
#     merge_chunks("reconstructed_file.dat")

# 13
# import os

# def replace_word(input_file, output_file, old_word, new_word):
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:

#         for line in infile:
#             updated_line = line.replace(old_word, new_word)
#             outfile.write(updated_line)

#     print("Replacement completed successfully!")


# if __name__ == "__main__":
#     base_path = os.path.dirname(os.path.abspath(__file__))
    
#     input_path = os.path.join(base_path, "largefile.txt")
#     output_path = os.path.join(base_path, "updated_largefile.txt")

#     replace_word(input_path, output_path, "ERROR", "WARNING")


# 14
# def extract_lines_with_keywords(input_file, output_file, keywords):
#     with open(input_file, 'r', encoding='utf-8') as infile, \
#          open(output_file, 'w', encoding='utf-8') as outfile:

#         for line in infile:
#             if all(keyword in line for keyword in keywords):
#                 outfile.write(line)

#     print("Extraction completed successfully!")


# if __name__ == "__main__":
#     keywords = ["ERROR", "Timeout"]
#     extract_lines_with_keywords("largefile.txt", 
#                                 "filtered_output.txt", 
#                                 keywords)


# 15 # Regex pattern for timestamp and message
# import re


# log_pattern = re.compile(
#     r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+)\s+\w+\s+(?P<message>.*)"
# )

# def parse_log_file(input_file):
#     with open(input_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             match = log_pattern.match(line)
            
#             if match:
#                 timestamp = match.group("timestamp")
#                 message = match.group("message")
                
#                 print("Timestamp:", timestamp)
#                 print("Message:", message)
#                 print("-" * 40)

# if __name__ == "__main__":
#     parse_log_file("app.log")


# 16
# def detect_malformed_rows(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         header = file.readline()
#         expected_columns = len(header.strip().split(','))

#         line_number = 1

#         for line in file:
#             line_number += 1
#             columns = len(line.strip().split(','))

#             if columns != expected_columns:
#                 print(f"Malformed row at line {line_number}: {line.strip()}")

# if __name__ == "__main__":
#     detect_malformed_rows("data.csv")

# 17
# def read_byte_range(file_path, start_byte, num_bytes):
#     with open(file_path, 'rb') as f:  
#         f.seek(start_byte)            
#         data = f.read(num_bytes)     


# if __name__ == "__main__":
#     data = read_byte_range("largefile.dat", 1024, 100)
#     print(data)

# 19
# import time
# import os

# def follow(file_path):
#     with open(file_path, "r") as file:
#         file.seek(0, os.SEEK_END)  # Move to end of file

#         while True:
#             line = file.readline()

#             if not line:
#                 time.sleep(0.5)  # Wait for new data
#                 continue

#             yield line


# if __name__ == "__main__":
#     for line in follow("app.log"):
#         print("New line:", line.strip())


# 20
import os
import time

def monitor_file(file_path):
    last_modified = os.path.getmtime(file_path)

    while True:
        current_modified = os.path.getmtime(file_path)

        if current_modified != last_modified:
            print("File has changed!")
            last_modified = current_modified

        time.sleep(1)


if __name__ == "__main__":
    monitor_file("app.log")
    