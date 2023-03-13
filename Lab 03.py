import math
x= float(input ("enter the x coordinate of the center of the circle: "))
y= float(input ("enter the y coordinates of the center of the circle: "))
x1= float(input("enter the x coordinate of a point on the circle: "))
y1= float(input("enter the y coordinates of a point on the circle: "))
r= (math.sqrt( (x1-x)**2 +(y1-y)**2))
c=2*3.1416*r

print("Circle Radius=", r )
print("Circle Circumference =", c)
