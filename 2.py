import image
def make_red_intense(img, intensity):
    win = image.ImageWin()
    old_img = image.Image(img)
    old_img.draw(win)
    
    width = old_img.getWidth()
    height = old_img.getHeight()
    new_img = image.EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            orig_pix = old_img.getPixel(col, row)
            new_pix = increase_red_intensity(orig_pix, intensity)
            new_img.setPixel(col, row, new_pix)
            
    new_img.setPosition(width + 1, 0)
    new_img.draw(win)
    win.exit_on_click()
    
def increase_red_intensity(pixel, intensity):
    r = pixel.getRed()
    g = pixel.getGreen()
    b = pixel.getBlue()
    r = r + intensity
    if r > 255:
        r = 255
    new_pixel = image.Pixel(r, g, b)
    return new_pixel


make_red_intense("butterfly.gif", 50)