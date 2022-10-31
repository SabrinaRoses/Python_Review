#Leia um valor de comprimento em jardas e apresente-o convertido em metros.
#A formula de conversão é: M = 0, 91 ∗ J

#Read a length value in yards and display it converted to meters

yards = float(input("Enter the value in Yards:\n"))

def yards_to_meters():
    """convert yards to meters"""
    meters = 0.91 * yards
    return print("The value converted to meters is:{: }m".format(meters))
   

#call the function
yards_to_meters()