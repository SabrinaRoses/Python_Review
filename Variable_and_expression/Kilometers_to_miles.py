#Leia uma distancia em quilômetros e apresente-a convertida em milhas.
#A formula para conversão é: M = K/1.61

#Read a distance in kilometers and display it converted to miles.

kilometers = float(input("Enter the distance in Kilometers:\n"))

def kilometers_to_miles():
    """Convert kilometers to miles"""
    miles = (kilometers/1.61)
    return print("The distance in miles is:{: }M".format(miles))

#call the function
kilometers_to_miles()