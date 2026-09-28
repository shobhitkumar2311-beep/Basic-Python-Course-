# Write a class “Calculator” capable of finding square, cube and square root of a number.

# Crarting the calss function
class calculator():
    def __init__(self, n):
        self.n = n

    # Creating the function for the square 
    def square(self):
        print(f"The square if {self.n * self.n}")

    # Creating the function for the cube 
    def cube(self):
        print(f"The cube if {self.n * self.n * self.n}")

    # Creating the function for the squareroot 
    def squareroot(self):
        print(f"The squareroot if {self.n ** 1/2 }")

# Taking input from the user
a = float(input("Enter the value: "))
cal = calculator(a)

# Calling the functions for the finding the answer
cal.square()
cal.cube()
cal.squareroot()
