# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

# import randint function to genrate random fare values
from random import randint

# Define a class 'Train' to represent a train
class train:
    # Constructor to initialize train number
    def __init__(self, train_no):
        self.train_no = train_no # Store train number in object
    # Method to book a ticket
    def book(self, fro, to):
        # Print booking confirmation with source and destination
        print(f"Ticket is booked in train no: {self.train_no} from {fro} to {to}")
    # Method to get train status (like seats or timing)
    def getstatus(self):
        # Print train running status
        print(f"Train no: {self.train_no} is runing on time.")
    # Method to get fare information
    def getfare(self, fro, to):
        # Genrate random fare between 100 and 10000
        fare = randint(100, 10000)
        # Print fare details
        print(f"Ticket fare in train no: {self.train_no} from {fro} to {to} is ₹{fare}")

# Create an object of train class with train number (12309)
t = train(12309)
# Take source station input from user
Source = input("Enter your source station point: ")
# Take destination station input from user
Distanation = input("Enter your distanation station point: ")
# Call book() method to book ticket
t.book(Source,Distanation)
# Call getstatus() method to check train status
t.getstatus()
# Call getfare() method to get ticket fare
t.getfare(Source,Distanation)


