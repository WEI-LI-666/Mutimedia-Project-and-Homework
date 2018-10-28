# Random Bezier Curve using De Casteljau's algorithm
# http://en.wikipedia.org/wiki/Bezier_curve
# http://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm
# FB - 201111244
import random, pygame, cmath
from PIL import Image, ImageDraw

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bezier Curve")
background_color = (250,250,250)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
white = (255, 255, 255)
mouse_pos = pygame.mouse.get_pos()
diameter=5
mouse_pressed=0
sel1=0
sel2=0
sel3=0
sel4=0

#imgx = 800
#imgy = 800
#image = Image.new("RGB", (imgx, imgy))
#draw = ImageDraw.Draw(image)

def B(coorArr, i, j, t):
    if j == 0:
        return coorArr[i]
    return B(coorArr, i, j - 1, t) * (1 - t) + B(coorArr, i + 1, j - 1, t) * t

def get_distance(x,y,xx,yy):
    return cmath.sqrt((x-xx)*(x-xx)-(y-yy)*(y-yy))

#n = random.randint(3, 6) # number of control points
n = 4
coorArrX = [200, 300, 500, 600]
coorArrY = [300, 100, 500, 300]

gameLoop = True
while(gameLoop):
    mouse_pressed=0 #reset mouse button
    window.fill(background_color) #redraw the screen
    mouse_pos = pygame.mouse.get_pos()#get mouse pos
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameLoop = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mouse_pressed=1
        if (event.type == pygame.MOUSEBUTTONUP):
            mouse_pressed=-1
    
    if abs(get_distance(coorArrX[0],coorArrY[0],mouse_pos[0],mouse_pos[1])) < diameter:
        if mouse_pressed:
            sel1=1
    if abs(get_distance(coorArrX[1],coorArrY[1],mouse_pos[0],mouse_pos[1])) < diameter:
        if mouse_pressed:
            sel2=1
    if abs(get_distance(coorArrX[2],coorArrY[2],mouse_pos[0],mouse_pos[1])) < diameter:
        if mouse_pressed:
            sel3=1
    if abs(get_distance(coorArrX[3],coorArrY[3],mouse_pos[0],mouse_pos[1])) < diameter:
        if mouse_pressed:
            sel4=1
    if sel1==1:
        coorArrX[0], coorArrY[0] = mouse_pos
        if mouse_pressed ==-1 :
            sel1=0
    if sel2==1:
        coorArrX[1], coorArrY[1] = mouse_pos
        if mouse_pressed ==-1 :
            sel2=0
    if sel3==1:
        coorArrX[2], coorArrY[2] = mouse_pos
        if mouse_pressed ==-1 :
            sel3=0
    if sel4==1:
        coorArrX[3], coorArrY[3] = mouse_pos
        if mouse_pressed ==-1 :
            sel4=0

    # plot the curve
    numSteps = 5000    
    for k in range(numSteps):
        t = float(k) / (numSteps - 1)
        x = int(B(coorArrX, 0, n - 1, t))
        y = int(B(coorArrY, 0, n - 1, t))
        try:
            #image.putpixel((x, y), (0, 255, 0))
            #pygame.gfxdraw.pixel(window, 100, 100, green)
            pygame.draw.line(window, green, (x, y), (x, y))
        except:
            pass

    for k in range(n):
        x = coorArrX[k]
        y = coorArrY[k]
        try:
            pygame.draw.circle(window, red, (x, y), diameter, 0)
        except:
            pass

    pygame.display.flip()
pygame.quit()