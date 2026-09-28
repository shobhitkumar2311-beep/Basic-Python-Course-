# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 


class demo():
    a = 4   # class variable

o = demo()  # create an object of class demo
print(o.a)  # prints value of 'a' from the class
o.a = 0     # assigns a new value to 'a' for this object only
print(o.a)  # prints the updated value of 'a' for this object

print(demo.a)# Prints the class attributr.
 