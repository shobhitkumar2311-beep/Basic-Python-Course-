# Add a static method in problem 2, to greet the user with hello

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

    @staticmethod # Static method does not depend on object data
    def hello():
        print("hello there!")


# Taking input from the user
a = float(input("Enter the value: "))
cal = calculator(a)

# Calling the functions for the finding the answer
cal.hello()
cal.square()
cal.cube()
cal.squareroot()
