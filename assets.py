import pygame
import os 

pygame.init()

window = pygame.display.set_mode((900,600),pygame.RESIZABLE)

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

running = True

fps = 60

clock = pygame.time.Clock()

favicon = pygame.image.load(f"{dir_path}/grass.jpg")
grass = pygame.transform.scale(pygame.image.load(f"{dir_path}/grass.jpg"),(200,200))
#menu_icon = pygame.transform.scale(pygame.image.load(f"{dir_path}/round invert logo.png"),(200,200))

########################
# CENTER AND OTHER LAYOUT SYSTEMS
########################

class center:
    def x(w):
        return (pygame.display.Info().current_w / 2) - (w / 2)
    def y(h):
        return (pygame.display.Info().current_h / 2) - (h / 2)

class button:
    def __init__(self,txt, size, color):
        self.color = color
        self.txt = text(size,str(txt),self.color)
    def render(self,x,y):
        self.txt.render(x,y)
    def hover(self,x,y):
        return (pygame.mouse.get_pos()[0] < x + self.txt.w and
                pygame.mouse.get_pos()[0] > x and
                pygame.mouse.get_pos()[1] < y + self.txt.h and
                pygame.mouse.get_pos()[1] > y)
    def click(self,x,y):
        if (pygame.mouse.get_pos()[0] < x + self.txt.w and
            pygame.mouse.get_pos()[0] > x and
            pygame.mouse.get_pos()[1] < y + self.txt.h and
            pygame.mouse.get_pos()[1] > y):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
        else:
            return False

########################
# TEXT
########################

class text:
    def __init__(self, size, text, color=(255,255,255)):
        self.font = pygame.font.Font(f"{dir_path}/font.ttf",size)
        self.color = color
        self.text_holder = text
        self.size_holder = size
        self.text = self.font.render(text, True, self.color)
        self.w = self.text.get_width()
        self.h = self.text.get_height()
    def render(self,x,y):
        self.font = pygame.font.Font(f"{dir_path}/font.ttf",self.size_holder)

        self.text = self.font.render(self.text_holder, True, (0,0,0))
        window.blit(self.text,(x,y - 2))
        window.blit(self.text,(x,y + 2))
        window.blit(self.text,(x - 2,y))
        window.blit(self.text,(x + 2,y))

        self.text = self.font.render(self.text_holder, True, self.color)
        window.blit(self.text,(x,y))
