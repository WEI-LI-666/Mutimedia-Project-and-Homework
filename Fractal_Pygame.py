import random, pygame, cmath, math, sys, InputBox
import numpy as np

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fractal")
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
count=0
textP=""
textL=""

clock = pygame.time.Clock()
inputP = InputBox.InputBox(725, 550-5)
inputL = InputBox.InputBox(725, 575-5)

n = 2
sel = np.zeros(n)
coorArrX = np.zeros(n)
coorArrY = np.zeros(n)
pol = np.zeros(n, int)
lev = np.zeros(n, int)


def Fractal(x1, y1, x2, y2, polygon, level):
    
    if polygon < 3:
        polygon = 1
    if polygon == 1 or level == 0:
        pygame.draw.line(window, green, [x1, y1], [x2,y2], 2)
    p = np.zeros((polygon, 2), int)
    angle = (polygon - 2) * 180.
    in_angle = float(angle / polygon)
    fix_angle = in_angle
    dx_angle = 180. - in_angle
    
    for i in range(polygon):
        if i == 0:
            p[i] = [(2. * x1 + x2) / 3., (2. * y1 + y2) / 3.]
        if i == polygon - 1:
            p[i] = [(x1 + 2. * x2) / 3., (y1 + 2. * y2) / 3.]
        if i != 0 and i != polygon - 1:
            A = np.matrix([[(1./3) * math.cos(math.radians(fix_angle)), (-1./3) * math.sin(math.radians(fix_angle))], 
                            [(-1./3) * math.sin(math.radians(fix_angle)), (-1./3) * math.cos(math.radians(fix_angle))]])
            if x2 <= x1 and y2 <= y1:
                A = np.matrix([[(1./3) * math.cos(math.radians(fix_angle + 180.)), (-1./3) * math.sin(math.radians(fix_angle))], 
                            [(-1./3) * math.sin(math.radians(fix_angle + 180.)), (-1./3) * math.cos(math.radians(fix_angle))]])           
            if x2 <= x1 and y2 >= y1:
                A = np.matrix([[(1./3) * math.cos(math.radians(fix_angle + 180.)), (-1./3) * math.sin(math.radians(fix_angle + 180.))], 
                            [(-1./3) * math.sin(math.radians(fix_angle + 180.)), (-1./3) * math.cos(math.radians(fix_angle + 180.))]])
            if x2 >= x1 and y2 >= y1:
                A = np.matrix([[(1./3) * math.cos(math.radians(fix_angle)), (-1./3) * math.sin(math.radians(fix_angle + 180.))], 
                            [(-1./3) * math.sin(math.radians(fix_angle)), (-1./3) * math.cos(math.radians(fix_angle + 180.))]])
            
            x = np.matrix([[float(abs(x1-x2))], [float(abs(y1-y2))]])
            b = np.matrix([[p[i-1][0]], [p[i-1][1]]])
            p[i] = (A * x + b).reshape((2,))

            fix_angle -= dx_angle
    
    if level == 1:
        pygame.draw.line(window, green, [x1, y1], p[0], 2)
        for pol in range(polygon-1):
            pygame.draw.line(window, green, p[pol], p[pol+1], 2)
        pygame.draw.line(window, green, p[polygon-1], [x2, y2], 2)  

    if(level > 0):
        level -= 1
        Fractal(x1, y1, p[0][0], p[0][1], polygon, level)
        for pol in range(polygon-1):
            Fractal(p[pol][0], p[pol][1], p[pol+1][0], p[pol+1][1], polygon, level)
        Fractal(p[polygon-1][0], p[polygon-1][1], x2, y2, polygon, level)       

def get_distance(x1,y1,x2,y2):
    return cmath.sqrt((x1-x2)*(x1-x2)-(y1-y2)*(y1-y2))

gameLoop = True
while(gameLoop):
    #clock.tick(30)
    mouse_pressed=0 #reset mouse button
    window.fill(background_color) #redraw the screen
    mouse_pos = pygame.mouse.get_pos()#get mouse pos
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameLoop = False
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if not (mouse_pos[0] > 625 and mouse_pos[0] < 800 and mouse_pos[1] > 545 and mouse_pos[1] < 600     # window's top-right and bottom-right won't do anything
                    or mouse_pos[0] > 700 and mouse_pos[0] < 800 and mouse_pos[1] > 0 and mouse_pos[1] < 145):
                mouse_pressed=1
                if count >= 2:
                    coorArrX = np.append(coorArrX, [0])
                    coorArrY = np.append(coorArrY, [0])
                    sel = np.append(sel, [0])
                    pol = np.append(pol, [0])
                    lev = np.append(lev, [0])
                coorArrX[count] = mouse_pos[0]
                coorArrY[count] = mouse_pos[1]
                count += 1
            if (mouse_pos[0] > 700 and mouse_pos[0] < 800 and mouse_pos[1] > 0 and mouse_pos[1] < 45):
                coorArrX = np.zeros(n)
                coorArrY = np.zeros(n)
                count=0
            if (mouse_pos[0] > 700 and mouse_pos[0] < 800 and mouse_pos[1] > 50 and mouse_pos[1] < 95):
                pol[count-1]=0
                lev[count-1]=0
            if (mouse_pos[0] > 700 and mouse_pos[0] < 800 and mouse_pos[1] > 100 and mouse_pos[1] < 145):
                if count > 2:
                    coorArrX = np.delete(coorArrX, -1, 0)
                    coorArrY = np.delete(coorArrY, -1, 0)
                else:
                    coorArrX[count-1] = 0.
                    coorArrY[count-1] = 0.
                count -= 1
        if (event.type == pygame.MOUSEBUTTONUP):
            mouse_pressed = -1
        inputP.handle_event(event)
        inputL.handle_event(event) 

    for i in range(count):
        if abs(get_distance(coorArrX[i],coorArrY[i],mouse_pos[0],mouse_pos[1])) < diameter:
            if mouse_pressed:
                sel[i]=1
        if sel[i]==1:
            coorArrX[i], coorArrY[i] = mouse_pos
            if mouse_pressed == -1:
                sel[i]=0

    inputP.draw(window)
    inputL.draw(window)
    textP = inputP.text_buf
    textL = inputL.text_buf

    if 700+100 > mouse_pos[0] > 700 and 0+45 > mouse_pos[1] > 0:
        pygame.draw.rect(window, bright_yellow,(700,0,100,45))
    else:
        pygame.draw.rect(window, yellow,(700,0,100,45))
    if 700+100 > mouse_pos[0] > 700 and 50+45 > mouse_pos[1] > 50:
        pygame.draw.rect(window, bright_yellow,(700,50,100,45))
    else:
        pygame.draw.rect(window, yellow,(700,50,100,45))
    if 700+100 > mouse_pos[0] > 700 and 100+45 > mouse_pos[1] > 100:
        pygame.draw.rect(window, bright_yellow,(700,100,100,45))
    else:
        pygame.draw.rect(window, yellow,(700,100,100,45))

    tfont = pygame.font.SysFont(None, 24, 1)
    tPol = tfont.render("Polygon: " + textP, 1, (0, 0, 0))
    tLev = tfont.render("Level: " + textL, 1, (0, 0, 0))
    clearText = tfont.render(str("Clear"), 0, (0, 0, 0))    # clear all lines and coordinates
    resetText = tfont.render(str("Reset"), 0, (0, 0, 0))    # set current fractal shape to default(pol=0, level=0)
    undoText = tfont.render(str("Undo"), 0, (0, 0, 0))     # remove latest coordinates and the fractal
    mp = tfont.render("mouse pos: " + str((mouse_pos[0],mouse_pos[1])), 0, (0, 0, 0))
    window.blit(tPol, (625, 550))
    window.blit(tLev, (649, 575))
    window.blit(mp, (300, 5))
    window.blit(clearText, (725, 15))
    window.blit(resetText, (725, 65))
    window.blit(undoText, (725, 115))

    if inputP.entered:
        if textP != None and len(textP) != 0:
            pol[count-1] = int(textP)
            if pol[count-1] > 10:
                pol[count-1] = 10
            inputP.entered = False

    if inputL.entered:
        if textL != None and len(textL) != 0:
            lev[count-1] = int(textL)
            if lev[count-1] > 10:
                lev[count-1] = 10
            inputL.entered = False
    
    for i in range(count):
        if i >= 1:
            Fractal(coorArrX[i-1], coorArrY[i-1], coorArrX[i], coorArrY[i], pol[i], lev[i])

    for p in range(count):
        x = coorArrX[p]
        y = coorArrY[p]
        try:
            pygame.draw.circle(window, red, (int(x), int(y)), diameter, 0)
        except:
            pass
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
