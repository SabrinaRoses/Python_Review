#Leia um valor de volume em metros cubicos m3 e apresente-o convertido em litros.
#A formula de conversão é igual L = 1000 * M

#Read a volume value in cubic meters m3 and present it converted into liters.



meters = float(input("Enter the value:\n"))

def meters_to_liters():
    """Convert meters to liters"""
    liters = 1000 * meters
    return print("The value converted into liters is:{: }L".format(liters))

#call the function
meters_to_liters()