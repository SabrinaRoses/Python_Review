#Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#A formula de conversão é: C = 5.0 ∗ (F − 32.0)/9.0

#Read a temperature in degress Fahrenheit and display it converted to degress Celsius.

fahrenheit_temperature = float(input("Enter the temperature in Fahrenheit:\n"))

def fahrenheit_to_celsius():
    """Convert fahrenheit to celsius"""
    celsius = 5.0 * (fahrenheit_temperature - 32.0)/9.0
    return print("The temperature in Celsius is:{: } C".format(celsius))

#call the function
fahrenheit_to_celsius()