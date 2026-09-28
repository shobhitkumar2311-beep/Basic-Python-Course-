# Write a program to find out the line number where python is present from ques 6.

# Open the file
with open ("Chapter-09/log2.html") as f:
    lines =  f.readlines()
line_no = 1
    # Checking according to the quwtions
for line in lines:
    if ("python" in line):  # If condition is true
        print(f"Yes, python is present in the file. Line no. : {line_no}")
        break
    line_no += 1 # Checking the line no in the file.

else:  # If condition is false
    print("No! python is not present in the file.") 