# Write a program to calculate the grade of a student from his marks from the following scheme: 
'''
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50     => F
'''
# To check if the student has passed or failed
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

sum = subject1 + subject2 + subject3
print("Total number in all subjects is given as: ", sum)
percentage = (sum / 300) * 100

if percentage>=100:
    print("Grade is : Ex")
elif percentage>=90:
    print("Grade is : A")
elif percentage>=80:
    print("Grade is : B")
elif percentage>=70:
    print("Grade is : C")
elif percentage>=60:
    print("Grade is : D")
elif percentage<=50:
    print("Grade is : F")
else:
    print("You are failed in the exam. Better luck next time.")
