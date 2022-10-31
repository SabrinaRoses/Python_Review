#Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s (metros por segundo).
#A formula de conversão e: M = K/3.6

#Read a speed in km/h (kilometers per hour) and display it converted to m/s (meters per second).

kilometers = float(input("Enter the km/h:\n"))

def kilometers_to_meters():
    """Convert kilometers to meters"""
    meters = (kilometers/3.6)
    return print("The kilometers per hour in meters per second is: {:.2f}m/s".format(meters))

#call the function
kilometers_to_meters()