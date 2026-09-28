# Write a python function which converts inches to cms. 

# Creating the function to convert the inches to cms
def inches_to_cms(inches):
    return inches * 2.54
# Taking input by the user
inches = float(input("Enter the value: "))
# Calling the function
value = inches_to_cms(inches)
print(f"{round(value,2)} centimeters is given by the {inches} inches")

# Creating the function to convert the cms to inches
def cms_to_inches(cms):
    return cms / 2.54
# Taking input by the user
cms = float(input("Enter the value: "))
# Calling the function
value = cms_to_inches(cms)
print(f"{round(value,2)} inches is given by the {cms} cms")
