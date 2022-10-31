#Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
#A formula de conversão é: P = C/2.54.

#Read a lenght value in centimeters and display it converted to inches.


centimeters = float(input("Enter the centimeters:\n"))

def centimeters_to_inch():
    """Convert centimeters to inches"""
    inches = (centimeters/2.54)
    return print("The value in inches is:{: }in".format(inches))

#call the function
centimeters_to_inch()


 