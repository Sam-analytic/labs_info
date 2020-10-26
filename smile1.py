import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((700, 700))
YELLOW = (225, 225, 0)
PURPLE = (255, 10, 102)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# face and eyes 
circle(screen, YELLOW, (350, 350),200)
circle(screen, PURPLE, (300,300),50)
circle(screen, PURPLE, (450,300),30)
#eyebrows 
polygon(screen, (0, 0, 0), [[200, 270],[360, 260], [350, 250], [200, 230]])
polygon(screen, (0, 0, 0), [[420, 270],[500, 250], [500, 280], [430, 280]])
#mouth
rect(screen, (0, 0, 0), (270, 400, 200, 70))
#tongue
circle(screen, RED, (360,490), 50)
rect(screen, YELLOW, (300, 470, 110, 70))
#teeth
polygon(screen, WHITE, [[300, 400], [350, 400], [325, 430]])
polygon(screen, WHITE, [[370, 400],[420, 400], [380, 430]])

pygame.display.update()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()