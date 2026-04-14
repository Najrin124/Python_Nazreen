import os

# print(os.getcwd())          # Current working directory
# os.chdir("/tmp")            # Change current working directory
# print(os.getcwd())   
# print(os.listdir(os.getcwd()))      # All entries in current dir
# print([f for f in os.listdir(".") if os.path.isfile(f)])  # Files only

# os.mkdir("new_dir")         # Single directory
# os.makedirs("a/b/c", exist_ok=True)  # Nested dirs (safe if exists)
# os.rmdir("new_dir")         # Remove empty dir
# os.removedirs("a/b/c")      # Remove nested dirs if empty

# open("sample.txt", "w").close()   # Create empty file
# os.remove("sample.txt")          # Delete file

# import os

# #Path Manipulation
# print(os.path.join("a", "b", "c.txt"))    # "a/b/c.txt"
# print(os.path.basename("/x/y/z.txt"))     # "z.txt"
# print(os.path.dirname("/x/y/z.txt"))      # "/x/y"
# print(os.path.exists("file.txt"))         # True/False
# print(os.path.isfile("file.txt"))         # True if file
# print(os.path.isdir("dir"))               # True if directory
# print(os.path.split("/x/y/z.txt"))        # ("/x/y", "z.txt")
# print(os.path.splitext("a.txt"))          # ("a", ".txt")

#Permissions & Metadata
# print(os.stat("test.txt"))          # File stats (size, times, permissions)
# print(os.path.getsize("test.txt"))  # File size in bytes
# print(os.path.getmtime("test.txt")) # Last modified timestamp

#Environment Variables
# print(os.environ["HOME"])            # Read
# os.environ["MY_VAR"] = "123"         # Set (process-local)
# print(os.getenv("MY_VAR", "default"))

#Running Commands / Processes
os.system("echo hello")              # Run a command (simple)
# More powerful: use subprocess module in real scripts

#Rename / Move
os.rename("test.txt", "new.txt")
os.replace("test3.txt", "final.txt")  # Safe replace
            