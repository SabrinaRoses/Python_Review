#Leia um valor de massa em quilogramas e apresente-o convertido em libras.
#A formula de conversão é: L = K/0,45.

#Read a mass value in kilograms and display it converted to pounds.

kilograms = float(input("Enter the value in kilograms:\n"))

def kilograms_to_pound():
    """Convert kilograms to pound"""
    pounds = (kilograms/0.45)
    return print("The value converted to pounds is:{: } pounds".format(pounds))

#call the function
kilograms_to_pound()