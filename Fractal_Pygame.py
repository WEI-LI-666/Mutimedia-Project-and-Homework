import random, pygame, cmath, math
import numpy as np

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fractal")
background_color = (150,150,150)
green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
white = (255, 255, 255)
mouse_pos = pygame.mouse.get_pos()
diameter=5
mouse_pressed=0
sel = []
sel1=0
sel2=0

n = 2
for i in range(n):
    sel.append(0)
    
coorArrX = [100, 700]
coorArrY = [450, 450]

def Fractal(x1, y1, x2, y2, polygon, level):
    p = np.zeros((polygon, 2))
    angle = (polygon - 2) * 180.
    in_angle = float(angle / polygon)
    fix_angle = in_angle
    if polygon < 3:
        polygon = 0
    if polygon == 0 or level == 0:
        pygame.draw.line(window, green, [x1, y1], [x2,y2], 2)

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

            fix_angle -= 180. - fix_angle
            if fix_angle < -90.: fix_angle += 90.

    #pygame.draw.line(window, green, [x1, y1], [x2, y2], 2)
    
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
            sel[0]=1
    if abs(get_distance(coorArrX[1],coorArrY[1],mouse_pos[0],mouse_pos[1])) < diameter:
        if mouse_pressed:
            sel[1]=1
    if sel[0]==1:
        coorArrX[0], coorArrY[0] = mouse_pos
        if mouse_pressed ==-1 :
            sel[0]=0
    if sel[1]==1:
        coorArrX[1], coorArrY[1] = mouse_pos
        if mouse_pressed ==-1 :
            sel[1]=0
    
    mfont = pygame.font.SysFont('Arial', 24, 1)
    pt1 = mfont.render(str((coorArrX[0], coorArrY[0])), 0, (0, 0, 0))
    pt2 = mfont.render(str((coorArrX[1], coorArrY[1])), 0, (0, 0, 0))
    m = mfont.render("mouse pos: " + str((mouse_pos[0],mouse_pos[1])), 0, (0, 0, 0))
    window.blit(m, (300, 0))
    window.blit(pt1, (0, 0))
    window.blit(pt2, (680, 0))

    #pygame.draw.line(window, green, (coorArrX[0], coorArrY[0]), (coorArrX[n-1], coorArrY[n-1]), 1)
    Fractal(coorArrX[0], coorArrY[0], coorArrX[1], coorArrY[1], 4, 2)

    for p in range(n):
        x = coorArrX[p]
        y = coorArrY[p]
        try:
            pygame.draw.circle(window, red, (x, y), diameter, 0)
        except:
            pass

    pygame.display.flip()
pygame.quit()
