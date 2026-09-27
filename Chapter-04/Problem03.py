# Check that a tuple type cannot be changed in python.
# Example: Tuples are immutable in Python

# Create a tuple
my_tuple = (10, 20, 30)
print("Original tuple:", my_tuple)

# Try to change an element of the tuple
# This will give an error because tuples cannot be modified
try:
    my_tuple[1] = 50   # Attempting to change value at index 1
except TypeError as e:
    print("Error:", e)  # Print the error message

# Tuple remains the same after the failed modification
print("Tuple after attempt:", my_tuple)
