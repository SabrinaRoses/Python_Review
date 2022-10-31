#Leia um valor de comprimento em metross e apresente-o convertido em jardas.
#A formula de conversão é: J = M/0,91

#Read a value in length meters and display it converted to yards

meters = float(input("Enter the value in meters:\n"))

def length_to_yards():
    """convert meters to yards"""
    yards = meters/0.91
    return print("The value converted to yards is:{: }Yards".format(yards))

#call the function
length_to_yards()
    