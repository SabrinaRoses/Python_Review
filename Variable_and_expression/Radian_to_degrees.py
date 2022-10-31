#Leia um angulo em radianos e apresente-o convertido em graus.
#A formula de conversão é: G = R ∗ 180/π, sendo G o angulo em graus e R em radianos e π = 3.14.

#Read an angle in radian and display it converted to degres.

import math

radian = float(input("Enter the radian angle:\n"))

def radian_to_degress():
    """Convert angle x from radians to degress"""
    x = math.degrees(radian)
    return print("The angle in radian converted to degrees is: {:.2f} degrees".format(x))

#call the function
radian_to_degress()

