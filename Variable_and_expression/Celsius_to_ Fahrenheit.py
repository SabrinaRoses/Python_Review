#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
#A formula de conversão F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

#Read a temperature in degrees Celsius and display it converted to degrees Fahrenheit.


celsius_temperature = float(input("Enter the temperature in Celsius:\n"))

def celsius_to_fahrenheit():
    """Convert to Fahrenheit"""

    fahrenheit = celsius_temperature*(9.0/5.0)+32.0
    return print("The value in Fahrenheit is:{: } F".format(fahrenheit))

#call the function   
celsius_to_fahrenheit()



