# Write a program to make a copy of a text file “this. txt”

# Reading the file
with open("Chapter-09/this.txt") as f:
    content = f.read()

# Copy the text for onr file to another file.
with open("Chapter-09/copy_this.txt","w") as f:
    f.write(content)

# "Copy_this.txt is used if problem10 for wipe"