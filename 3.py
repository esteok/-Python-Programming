import image

def enlarge_image(old_img,x_scale,y_scale):
    old_width = old_img.getWidth()
    old_height = old_img.getHeight()
    new_img = image.EmptyImage(old_width * x_scale, old_height * y_scale)
    
    new_width = new_img.getWidth()
    new_height = new_img.getHeight()
    
    for row in range (new_height):
        for col in range(new_width):
            old_col = col // x_scale
            old_row = row // y_scale
            old_pix = old_img.getPixel(old_col,old_row)
            new_img.setPixel(col,row,old_pix)
    return new_img

def make_enlarge_img(img,x_scale,y_scale):
    old_img=image.FileImage(img)
    width = old_img.getWidth()   
    height = old_img.getHeight()

    new_img = enlarge_image(old_img,x_scale,y_scale)
    window = image.ImageWin(width*x_scale, height*(1+y_scale)) 
    new_img.draw(window)
    window.exitOnClick()

make_enlarge_img("butterfly.gif",3,3)