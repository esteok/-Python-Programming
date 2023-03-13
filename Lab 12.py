from cImage import *

myImage = ImageWin("Image", 300, 300)
image = EmptyImage(300, 300)

g = Pixel(0, 255, 0)
r = Pixel(255, 0, 0)

for i in range(150, 300):
    image.setPixel (i, i, r)
for i in range(300):
    image.setPixel (i, 150, g)
for i in range(300):
    image.setPixel(150, i, g)


image.draw(myImage)
Image.exitonClick()
    
