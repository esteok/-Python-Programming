import image
def makeBlackNWhite(img):
    win = image.ImageWin()
    old_img = image.Image(img)
    old_img.draw(win)
    
    width = old_img.getWidth()
    height = old_img.getHeight()
    new_img = image.EmptyImage(width, height)
    
    for row in range(height):
        for col in range(width):
            orig_pix = old_img.getPixel(col, row)
            new_pix = blackPixel(orig_pix)
            new_img.setPixel(col, row, new_pix)
            
    new_img.setPosition(width + 1, 0)
    new_img.draw(win)
    win.exit_on_click()
    
def blackPixel(pixel):
    intensity_sum = pixel.getRed() + pixel.getGreen() + pixel.getBlue()
    avg_RGB = intensity_sum // 3
    if avg_RGB > 150:
        rgb = 255
    else:
        rgb = 0
    new_pixel = image.Pixel(rgb, rgb, rgb)
    return new_pixel


makeBlackNWhite("cy.png")