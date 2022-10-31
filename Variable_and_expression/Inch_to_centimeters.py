#Leia um valor de comprimento em polegadas e apresente-o convertido em centımetros.
#A formula de conversão é: C = P ∗ 2.54.

#Read a lenght value in inches and display it converted to centimeters. 

inch = float(input("Enter the lenght value:\n"))

def inch_to_centimeters():
    """Convert inch to centimeters"""
    centimeters = inch * 2.54
    return print("The value in centimeters is:{: }cm".format(centimeters))

#call the function
inch_to_centimeters()