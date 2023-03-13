import math

def sphere_volume(radius):
    vol = (4 / 3) * math.pi * pow(radius, 3)
    return vol

rad = float(input("enter the radius of a sphere: "))
print(sphere_volume(rad))
