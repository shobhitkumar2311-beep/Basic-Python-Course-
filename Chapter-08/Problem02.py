# Write a python program using function to convert Celsius to Fahrenheit. 

# Creating the function to convert the celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Taking input by the user
celsius = float(input("Enter the temprature: "))
# Calling the function
temprature = celsius_to_fahrenheit(celsius)
print(f"{round(temprature,2)} °C tempratute is given.")


# Creating the function to convert the fahrenheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
# Taking input by the user
fahrenheit = float(input("Enter the temprature: "))
# Calling the function
temprature = fahrenheit_to_celsius(fahrenheit)
print(f"{round(temprature,2)} °C tempratute is given.")
 