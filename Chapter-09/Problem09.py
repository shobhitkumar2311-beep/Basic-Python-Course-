# Write a program to find out whether a file is identical & matches the content of another file.


# Reading first file
with open("Chapter-09/file1.txt") as f:
    content1 = f.read()

# Reading seccond file
with open("Chapter-09/file2.txt") as f:
    content2 = f.read()

# Comparing the file with each statment if any one statement is missing then answer will be not identical and matches.
if (content1 == content2):
    print("Yes, file is identical and matches the content of another file.")
else:
    print("No! file is not identical and matches the content of another file.")
