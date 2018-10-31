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
P_entered = 0
textL=""
L_entered = 0

n = 2
sel = np.zeros(n)
coorArrX = np.zeros(n)
coorArrY = np.zeros(n)
pol = np.zeros(n, int)

def display_box(window, text):
    font = pygame.font.Font(None, 18)
    Pol_box = pygame.Rect(0, 0, 220, 22)

    win_center = window.get_rect().center
    Pol_box.center = win_center
    Pol_box.bottom = 600

    pygame.draw.rect(window, (0, 0, 0), Pol_box, 0)
    pygame.draw.rect(window, (255, 255, 255), Pol_box, 1)

    Pol_box.top += 3
    Pol_box.left += 3

    if len(text) != 0:
        window.blit(font.render(text, 1, white), Pol_box.topleft)

    #pygame.display.flip()


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

display_box(window, "Polygon: " + textP)
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
            if count >= 2:
                coorArrX = np.append(coorArrX, [0])
                coorArrY = np.append(coorArrY, [0])
                sel = np.append(sel, [0])
                pol = np.append(pol, [0])
            coorArrX[count] = mouse_pos[0]
            coorArrY[count] = mouse_pos[1]
            count += 1
        if (event.type == pygame.MOUSEBUTTONUP):
            mouse_pressed=-1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                textP = textP[0:-1]
                P_entered = 0
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                P_entered = 1
                break
            else:
                textP += event.unicode.encode("ascii")
    
    for i in range(count):
        if abs(get_distance(coorArrX[i],coorArrY[i],mouse_pos[0],mouse_pos[1])) < diameter:
            if mouse_pressed:
                sel[i]=1
        if sel[i]==1:
            coorArrX[i], coorArrY[i] = mouse_pos
            if mouse_pressed == -1:
                sel[i]=0

    '''if abs(get_distance(coorArrX[0],coorArrY[0],mouse_pos[0],mouse_pos[1])) < diameter:
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
            sel[1]=0'''
    
    mfont = pygame.font.SysFont('Arial', 20, 1)
    pt1 = mfont.render(str((coorArrX[0], coorArrY[0])), 0, (0, 0, 0))
    pt2 = mfont.render(str((coorArrX[1], coorArrY[1])), 0, (0, 0, 0))
    m = mfont.render("mouse pos: " + str((mouse_pos[0],mouse_pos[1])), 0, (0, 0, 0))
    window.blit(m, (300, 0))
    window.blit(pt1, (0, 0))
    window.blit(pt2, (680, 0))

    display_box(window, "Polygon: " + textP)

    if P_entered == 1:
        if textP != None and len(textP) != 0:
            pol[count-1] = int(textP)
            if pol[count-1] > 10:
                textP = "10"
                pol[count-1] = 10
    for i in range(count):
        Fractal(coorArrX[count-2], coorArrY[count-2], coorArrX[count-1], coorArrY[count-1], pol[count-1], 2)

    for p in range(count):
        x = coorArrX[p]
        y = coorArrY[p]
        try:
            pygame.draw.circle(window, red, (int(x), int(y)), diameter, 0)
        except:
            pass
    print count
    pygame.display.flip()
pygame.quit()
