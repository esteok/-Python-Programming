xcoordinate = int(input("Enter the x-coordinate "))
ycoordinate = int(input("Enter the y-coordinate "))
radius = int(input("Enter the radius "))

def inCircle(x,y,r):
    if x**2 + y**2 <= r**2:
        print("Point (", x, ",","",y, ") " "is in the circle with radius")
        return True
    else:
        print("Point (", x, ",","",y, ") " "is not in the circle with radius", radius)
        return False

inCircle(xcoordinate,ycoordinate,radius)
