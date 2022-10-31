#Leia um valor de massa em libras e apresente-o convertido em quilogramas.
#A formula é: K = L*0.45.

#Read a mass value in pounds and present it converted to kilograms.

pounds = float(input("Enter the value in pounds:\n"))

def pounds_to_kilograms():
    """convert pounds to kilograms"""
    kilograms = (pounds*0.45)
    return print("The value converted to kilograms is:{: }kg".format(kilograms))

#call the function
pounds_to_kilograms()