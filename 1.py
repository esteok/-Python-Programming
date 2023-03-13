import image
import math
WIN_WIDHT = 640
WIN_HEIGHT = 640
def create_circle(center_x,center_y,radius):
    win=image.ImageWin(WIN_WIDHT,WIN_HEIGHT)
    img=image.EmptyImage(WIN_WIDHT,WIN_HEIGHT)
   
    radians_value=[]
    for i in range(361):
        radians_value.append(math.radians(i))
        
    x_list=[]
    for i in radians_value:
        x_list.append(int(math.cos(i)*radius))

    y_list=[]
    for i in radians_value:
        y_list.append(int(math.sin(i)*radius))

    pixel=image.Pixel(0,0,0)
    
    for i in range(len(x_list)):
        
        x=x_list[i]+center_x
        y=y_list[i]+center_y
        img.set_pixel(x,y,pixel)
    img.draw(win)
    win.exit_on_click()

if __name__=="__main__":
    create_circle(320,320,50)
