# Random Bezier Curve using De Casteljau's algorithm
# http://en.wikipedia.org/wiki/Bezier_curve
# http://en.wikipedia.org/wiki/De_Casteljau%27s_algorithm
import random, pygame, cmath
import numpy as np

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bezier Curve")
background_color = (150,150,150)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255, 185, 0)
bright_yellow = (255, 220, 0)
white = (255, 255, 255)
mouse_pos = pygame.mouse.get_pos()
diameter=5
mouse_pressed=0
sel1=0
sel2=0
sel3=0
sel4=0
count=0

# number of control points
n = 4
coorArrX = np.zeros(n)
coorArrY = np.zeros(n)

def B(coorArr, i, j, t):
    if j == 0:
        return coorArr[i]
    return B(coorArr, i, j - 1, t) * (1 - t) + B(coorArr, i + 1, j - 1, t) * t

def get_distance(x,y,xx,yy):
    return cmath.sqrt((x-xx)*(x-xx)-(y-yy)*(y-yy))

def clear_B():
    coorArrX.fill(0.)
    coorArrY.fill(0.)

gameLoop = True
while(gameLoop):
    mouse_pressed=0 #reset mouse button
    window.fill(background_color) #redraw the screen
    mouse_pos = pygame.mouse.get_pos()#get mouse pos
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameLoop = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mouse_pressed = 1
            if count < 4 and not (mouse_pos[0] > 700 and mouse_pos[1] < 50):
                mouse_pressed=1
                coorArrX[count] = mouse_pos[0]
                coorArrY[count] = mouse_pos[1]
                count += 1
            if mouse_pos[0] > 700 and mouse_pos[1] < 50:
                count=0
                clear_B()
        if (event.type == pygame.MOUSEBUTTONUP):
            mouse_pressed=-1
    
    if count > 3:
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
        numSteps = 3000    
        for k in range(numSteps):
            t = float(k) / (numSteps - 1)
            x = int(B(coorArrX, 0, n - 1, t))
            y = int(B(coorArrY, 0, n - 1, t))
            try:
                pygame.draw.line(window, green, (x, y), (x, y), 2)
            except:
                pass

    if 700+100 > mouse_pos[0] > 700 and 0+50 > mouse_pos[1] > 0:
        pygame.draw.rect(window, bright_yellow,(700,0,100,50))
    else:
        pygame.draw.rect(window, yellow,(700,0,100,50))

    mfont = pygame.font.SysFont(None, 24, 1)
    pt1 = mfont.render("coorArrX: "+str(coorArrX), 0, (0, 0, 0))
    pt2 = mfont.render("coorArrY: "+str(coorArrY), 0, (0, 0, 0))
    buttonText = mfont.render(str("Clear"), 0, (0, 0, 0))
    m = mfont.render("mouse pos: " + str((mouse_pos[0],mouse_pos[1])), 0, (0, 0, 0))
    window.blit(buttonText, (725, 15))
    window.blit(m, (300, 0))
    window.blit(pt1, (0, 25))
    window.blit(pt2, (0, 50))

    for k in range(count):
        x = coorArrX[k]
        y = coorArrY[k]
        try:
            pygame.draw.circle(window, red, (int(x), int(y)), diameter, 0)
        except:
            pass

    pygame.display.flip()
pygame.quit()