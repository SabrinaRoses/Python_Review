#Leia um angulo em graus e apresente-o convertido em radianos.
# A formula de conversão é:  R = G ∗ π/180, sendo G o angulo em graus e R em radianos e π = 3.14.

#Read a angle in degress and display it converted to radian.

import math

angle_x = float(input("Enter the angle in degrees:\n"))

def angle_to_radian():
    """convert angle x from degrees to radians"""
    x = math.radians(angle_x)
    return print("The angle degress converted in radian is: {:.2f} radian.".format(x))

#call the function
angle_to_radian()