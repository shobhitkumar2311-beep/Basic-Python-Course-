# Write a program to mine a log file and find out whether it contains ‘python’.

# Open the file
with open ("Chapter-09/log1.html", "r") as f:
    content = f.read()
    # Checking according to the quwtions

if ("python" in content):  # If condition is true
    print("Yes, python is present in the file.")
else:  # If condition is false
    print("No! python is not present in the file.") 