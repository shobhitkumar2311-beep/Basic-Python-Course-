# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects. 
# import randint function to generate random fare values
from random import randint

# Define a class 'Train' to represent a train
class Train:
    # Constructor to initialize train number
    def __init__(slf, train_no):   # 'harry' is used instead of 'self'
        slf.train_no = train_no    # Store train number in object

    # Method to book a ticket
    def book(harry, fro, to):        # 'harry' refers to the object
        print(f"Ticket is booked in train no: {harry.train_no} from {fro} to {to}")

    # Method to get train status
    def getstatus(harry):
        print(f"Train no: {harry.train_no} is running on time.")

    # Method to get fare information
    def getfare(harry, fro, to):
        fare = randint(10, 1000)   # Generate random fare
        print(f"Ticket fare in train no: {harry.train_no} from {fro} to {to} is ₹{fare}")


# Create an object of Train class with train number (12309)
t = Train(12309)

# Take source station input from user
Source = input("Enter your source station point: ")

# Take destination station input from user
Destination = input("Enter your destination station point: ")

# Call book() method to book ticket
t.book(Source, Destination)

# Call getstatus() method to check train status
t.getstatus()

# Call getfare() method to get ticket fare
t.getfare(Source, Destination)
