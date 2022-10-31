#Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h(quilometros por hora).
#A fórmula de conversão é: K = M ∗ 3.6

#Read a speed in m/s (Meters per second) and display it converted to km/h (Kilometers to hour).

meters = float(input("Enter the m/s:\n"))

def meters_to_kilometers():
    """Convert meters to kilometers"""
    kilometers = meters * 3.6
    return print("The Meters (Per sencond) in Kilometers (Per hour) is: {:.2f}km/h".format(kilometers))

#call the function
meters_to_kilometers()