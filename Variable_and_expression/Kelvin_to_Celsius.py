#Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
# Aformula de conversão é: C = K − 273.15.

#Read a temperature in degress Kelvin and display it converted in degress Celsius.

kelvin_temperture = float(input("Enter the Kelvin temperature:\n"))

def kelvin_to_celsius():
    """Convert Kelvin to Celsius"""
    celsius = kelvin_temperture - 273.15
    return print ("The temperature in Celsius is:{: } C".format(celsius))

#call the function
kelvin_to_celsius()