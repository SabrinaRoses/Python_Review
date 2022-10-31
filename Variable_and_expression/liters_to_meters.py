#Leia um valor de volume em litros e apresente-o convertido em metros cubicos
#A formula é: M = L/1000

#Read a volume value in liters and display it converted into cubic meters.

liters = float(input("Enter the value in liters:\n"))

def liters_to_meters():
    """convert liters to meters"""
    meters = (liters/1000)
    return print("The valued converted to meters is:{: }m^3".format(meters))

#call the function
liters_to_meters()