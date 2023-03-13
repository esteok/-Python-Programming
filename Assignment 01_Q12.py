import turtle
t= turtle.Turtle()

def square(t,side):
    for x in range(4):
        t.forward(side)
        t.left(90)
    t.up()
    t.forward(5)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.down()
            


square(t,200)
square(t,190)
square(t,180)
square(t,170)
square(t,160)
square(t,150)
square(t,140)
square(t,130)
sqaure(t,120)
square(t,110)

