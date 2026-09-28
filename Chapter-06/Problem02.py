# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

# To check if the student has passed or failed
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

sum = subject1 + subject2 + subject3
print("Total number in all subjects is given as: ", sum)
percentage = (sum / 300) * 100

if (subject1 >= 33) and (subject2 >= 33) and (subject3 >= 33) and (percentage >= 40):
    print("The student will be passed.")
else:
    print("The student will be failed due to poor marks in examination.")


