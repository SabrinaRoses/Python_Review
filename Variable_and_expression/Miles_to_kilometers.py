#Leia uma distancia em milhas e apresente-a convertida em quilômetros.
# A fórmula de conversão é: K = 1,61 ∗ M.

#Read a distance in miles and display it converted to kilometers.

distance = float(input("Enter the distance in miles:\n"))

def miles_to_kilometers():
    """Convert miles to kilometers"""
    kilometers = 1.61 * distance
    return print("The distance in kilometers is:{: }km".format(kilometers))

#call the function
miles_to_kilometers()