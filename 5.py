import image
FACTOR = 2
window = image.ImageWin()
img = image.Image("cy.png")
width= img.getWidth()
height= img.getHeight()
new_width = int(width*FACTOR)
new_height = int(height*FACTOR)
new_img = image.EmptyImage(new_width, new_height)
for column in range(new_width):
  for row in range(new_height):
    x = column/FACTOR
    y = row/FACTOR
    p = img.getPixel(x,y)
    new_img.setPixel(column,row,p)
    
new_img.draw(window)
window.exitonclick()
