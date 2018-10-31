import pygame, re

class InputBox():
    
    def __init__(self, x, y):

        self.font = pygame.font.Font(None, 24)

        self.inputBox = pygame.Rect(x, y, 75, 25)

        self.colourInactive = pygame.Color('lightskyblue3')
        self.colourActive = pygame.Color('dodgerblue2')
        self.colour = self.colourInactive

        self.text = ''
        self.text_buf = ''
        self.pattern = re.compile(r'[0-9]+')

        self.active = False
        self.isBlue = True
        self.entered = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    #print(self.text)
                    self.text_buf = self.text
                    self.entered = True
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 2:
                        self.matcher = self.pattern.match(event.unicode)
                        if self.matcher:
                            self.text += event.unicode
                        

    def draw(self, screen):

        pygame.draw.rect(screen, (255, 255, 255), self.inputBox, 0)
        txtSurface = self.font.render(self.text, True, self.colour)
        width = max(75, txtSurface.get_width()+10)
        self.inputBox.w = width
        screen.blit(txtSurface, (self.inputBox.x+5, self.inputBox.y+5))
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)

        if self.isBlue:
            self.color = (0, 128, 255)
        else:
            self.color = (255, 100, 0)
