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

def Fractal(x1, x2, y1, y2, polygon, level):
    pt = np.zeros((5, 2))
    if polygon < 3:
        polygon = 0
    if level < 2:
        level = 0
    pt[0] = [x1, y1]
    pt[polygon + 1] = [x2, y2]
    for i in range(1, polygon):
        pt[i] = (pt[0] + pt[polygon+1]) * (1.0/polygon) * i
    if polygon == 0 or level == 0:
        pygame.draw.line(window, green, pt[0], pt[polygon+1], 1)

    return Fractal(p[0])

def get_distance(x1,y1,x2,y2):
    return cmath.sqrt((x1-x2)*(x1-x2)-(y1-y2)*(y1-y2))

n = 2
for i in range(n):
    sel.append(0)
coorArrX = [100, 700]
coorArrY = [300, 300]

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
    window.blit(pt1, (0, 0))
    window.blit(pt2, (680, 0))

    pygame.draw.line(window, green, (coorArrX[0], coorArrY[0]), (coorArrX[n-1], coorArrY[n-1]), 1)

    for p in range(n):
        x = coorArrX[p]
        y = coorArrY[p]
        try:
            pygame.draw.circle(window, red, (x, y), diameter, 0)
        except:
            pass

    pygame.display.flip()
pygame.quit()
