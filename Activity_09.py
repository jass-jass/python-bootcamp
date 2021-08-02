import math
print ("Enter dimensions :")
l = int(input("length :  "))
b = int(input("breadth:  "))
h = int(input("height :  "))
k = l**2 + b**2 + h**2
volume = b**2 * h**2 / k**(1/2)
print ("Volume of Tromboloid is %.3f"%volume)
radius = (3 * volume / (4*math.pi)) ** (1/3)
print ("Equivalent spherical radius is %.3f" %radius)
