# Label the program written in problem 4 with comments.

# Program to print contents of a directory using os module
import os

# specify the directory path
directory_path = "."

# list all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory in the contents
print(contents)