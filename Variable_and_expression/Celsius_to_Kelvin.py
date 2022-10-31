#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
# Aformula de conversão é: K = C + 273.15

#Read a temperature in degress Celsius and display it converted to degress Kelvin.

celsius_temperatue = float(input("Enter the Celsius temperature\n"))

def celsius_to_kelvin():
    """Convert the temperature to kelvin"""
    kelvin = celsius_temperatue + 273.15
    return print("The temperature in Kelvin is:{: } K".format(kelvin))
    
#call the function
celsius_to_kelvin()