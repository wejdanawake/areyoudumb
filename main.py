import pygame, sys, random

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 60
W, H = 512, 512
SCREEN = pygame.display.set_mode((W, H)) # make pygame window
TITLE = pygame.display.set_caption("Are you dumb? ")
ICON = pygame.image.load("assets\images\icon.png")
pygame.display.set_icon(ICON)

colors = {
    "white" : (255, 255, 255),
    "gray" : (20, 20, 20),
    "lightgray" : (50, 50, 50),
    "lightergray" : (100, 100, 100),
    "black" : (0, 0, 0)}


MOUSE = pygame.mouse.get_pos()
dumb = False

font = pygame.font.Font("assets\\fonts\\roboto.ttf", 48)
font_small = pygame.font.Font("assets\\fonts\\roboto.ttf", 24)

text_surf = font.render("Are You Dumb?", True, colors["red"])
text_rect = text_surf.get_rect(midbottom = (W/2, H/3))
finaltext_surf = font.render("I knew it! ", True, colors["red"])
finaltext_rect = finaltext_surf.get_rect(center = (W/2, H/2))

def reset():
    global dumb
    dumb = False
    button_no.center = (W/4*3, H/3*2)
    button_yes.center = (W/4, H/3*2)

class Button:
    def __init__(self, center, text):
        self.center = center
        self.text = text
        self.size = int(W/7)
        self.surf = pygame.surface.Surface((self.size, self.size))
        self.rect = self.surf.get_rect(center = self.center)
        self.text_surf = font_small.render(self.text, True, colors["white"])
        self.color = colors["gray"]
        self.hover = False
        self.clicked = False


    def draw(self):
        self.rect = self.surf.get_rect(center = self.center)
        self.text_rect = self.text_surf.get_rect(center = self.center)
        pygame.draw.polygon(SCREEN, self.color, [
            self.rect.topleft,
            self.rect.topright,
            self.rect.bottomright,
            self.rect.bottomleft
        ])
        pygame.draw.lines(SCREEN, colors["white"], True,
        (self.rect.topright, self.rect.topleft, self.rect.bottomleft, self.rect.bottomright)
        )
        
        if self.hover:
            self.color = colors["lightgray"]
            if self.clicked:
                self.color = colors["lightergray"]
        else:
            self.color = colors["gray"]

        SCREEN.blit(self.text_surf, self.text_rect)


    def reposition(self):
        self.center = (random.choice(range(int(W/2), int(W - self.size/2))), 
            random.choice(range(int(H/2), int(H - self.size/2))))

button_yes = Button((W/4, H/3*2), "Yes")
button_no = Button((W/4*3, H/3*2), "No")


def main():
    global MOUSE, dumb
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dumb:
                        reset()

            MOUSE = pygame.mouse.get_pos()
            if button_yes.rect.collidepoint(MOUSE):
                button_yes.hover = True
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    button_yes.clicked = True
            else:
                button_yes.hover = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                button_yes.clicked = False
                if dumb:
                    reset()
                if button_yes.rect.collidepoint(MOUSE):
                    dumb = True
                    
            if button_no.rect.collidepoint(MOUSE):
                button_no.reposition()


        SCREEN.fill(colors["gray"])
        SCREEN.blit(text_surf, text_rect)
        button_yes.draw()
        button_no.draw() 


        if dumb:
            button_yes.rect.bottomright = (0,0)
            SCREEN.fill(colors["gray"])
            SCREEN.blit(finaltext_surf, finaltext_rect)
            

        CLOCK.tick(FPS)
        pygame.display.update()
main()