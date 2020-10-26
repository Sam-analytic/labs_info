import pygame
from pygame.draw import *

pygame.init()

#Redacting  --   File "smile2.2.py", line 113, in lama
#    pygame.draw.circle(screen, WHITE, (x+200*Q, y+730*Q), 10*Q)
# TypeError: integer argument expected, got float          ----- needs to be rectified but the code is hard coded, no space for rectification. Need to make functions to accept arguments to draw objects rather than hard coding objects.


FPS = 30
screen = pygame.display.set_mode((800, 800))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SteelBlue = (105, 105, 105)
SkyBlue = (135, 206, 235)
DarkOrange = (255, 140, 0)
Gold = (255, 215, 0)
YellowGreen = (154, 205, 50)
LightGreen = (144, 238, 144)
Olive = (107, 142, 35)
Yellow = (255, 255, 0)
WHITE1 = (255, 239, 213)
SeaGreen = (46, 139, 87)
Pale = (175, 238, 238)

#фон
pygame.draw.rect(screen, SkyBlue, (0, 0, 800, 400))
pygame.draw.circle(screen, Gold, (750,200 ), 150)
pygame.draw.circle(screen, DarkOrange, (750, 200 ), 100)
pygame.draw.polygon(screen, SteelBlue, [[0,430], [0,300], [200, 100], [300,200], [400,20], [550,100], [600,200] ,[650,140], [750,300], [800,230], [800,430]])
pygame.draw.rect(screen, YellowGreen, (0, 430, 800, 400))
pygame.draw.ellipse(screen, LightGreen, (500, 460, 400, 200))
pygame.draw.ellipse(screen, LightGreen, (0, 570, 356, 200))

pygame.draw.polygon(screen, SeaGreen, [[0,430], [0,420], [20, 380], [10,380],[30,350],[50,380], [40,380], [70,430]])
pygame.draw.polygon(screen, SeaGreen, [[100,430], [100,420], [120, 380], [110,380],[130,350],[150,380], [140,380], [170,430]])
pygame.draw.polygon(screen, SeaGreen, [[150,430], [150,420], [170, 380], [160,380],[180,350],[200,380], [190,380], [220,430]])
pygame.draw.polygon(screen, SeaGreen, [[300,430], [300,420], [320, 380], [310,380],[330,350],[350,380], [340,380], [370,430]])
pygame.draw.polygon(screen, SeaGreen, [[400,430], [400,420], [420, 380], [410,380],[430,350],[450,380], [440,380], [470,430]])
pygame.draw.polygon(screen, SeaGreen, [[600,430], [600,420], [620, 380], [610,380],[630,350],[650,380], [640,380], [670,430]])
pygame.draw.polygon(screen, SeaGreen, [[700,430], [700,420], [720, 380], [710,380],[730,350],[750,380], [740,380], [770,430]])

#ромашка
pygame.draw.ellipse(screen, WHITE1, (610,500, 30, 15))
pygame.draw.ellipse(screen, WHITE1, (615,480, 30, 20))
pygame.draw.ellipse(screen, WHITE1, (640,470, 20, 30))
pygame.draw.ellipse(screen, WHITE1, (640,480, 30, 20))
pygame.draw.ellipse(screen, WHITE1, (645,490, 40, 20))
pygame.draw.ellipse(screen, WHITE1, (640,495, 20, 40))

pygame.draw.circle(screen, Yellow, (644,500 ), 10)

pygame.draw.ellipse(screen, WHITE1, (696,500, 30, 15))
pygame.draw.ellipse(screen, WHITE1, (710,480, 30, 20))
pygame.draw.ellipse(screen, WHITE1, (726,470, 20, 30))
pygame.draw.ellipse(screen, WHITE1, (720,490, 40, 30))
pygame.draw.ellipse(screen, WHITE1, (720,492, 18, 35))

pygame.draw.circle(screen, Yellow, (730,500 ), 10)

pygame.draw.ellipse(screen, WHITE1, (610,580, 30, 15))
pygame.draw.ellipse(screen, WHITE1, (615,560, 30, 20))
pygame.draw.ellipse(screen, WHITE1, (640,550, 20, 30))
pygame.draw.ellipse(screen, WHITE1, (640,560, 30, 20))
pygame.draw.ellipse(screen, WHITE1, (645,570, 40, 20))
pygame.draw.ellipse(screen, WHITE1, (640,575, 20, 40))

pygame.draw.circle(screen, Yellow, (640,580 ), 10)

pygame.draw.ellipse(screen, WHITE1, (540,595, 30, 15))
pygame.draw.ellipse(screen, WHITE1, (545,590, 30, 20))
pygame.draw.ellipse(screen, WHITE1, (560,600, 20, 30))
pygame.draw.ellipse(screen, WHITE1, (550,600, 20, 40))
pygame.draw.ellipse(screen, WHITE1, (570,600, 40, 20))
pygame.draw.ellipse(screen, WHITE1, (570, 595, 20, 40))

pygame.draw.circle(screen, Yellow, (570,610 ), 10)

pygame.draw.ellipse(screen, WHITE1, (536,530, 30, 15))
pygame.draw.ellipse(screen, WHITE1, (540,510, 30, 20))
pygame.draw.ellipse(screen, WHITE1, (550,520, 40, 30))
pygame.draw.ellipse(screen, WHITE1, (560,512, 18, 35))

pygame.draw.circle(screen, Yellow, (565,531 ), 10)



def lama(x, y, size):
     Q = size/10
     print(x,y)
#shadow
     pygame.draw.ellipse(screen, Olive, (x+100*Q, y+680*Q, 300*Q, 100*Q))
#lama
     pygame.draw.polygon(screen, WHITE, [[x+200*Q, y+530*Q], [x+400*Q, y+530*Q], [x+400*Q, y+610*Q], [x+200*Q, y+610*Q],[x+170*Q, y+560*Q]])
     pygame.draw.ellipse(screen, WHITE, (x+380*Q, y+530*Q, 40*Q, 80*Q))
     pygame.draw.ellipse(screen, WHITE, (x+180*Q, y+550*Q, 60*Q, 100*Q))
     pygame.draw.ellipse(screen, WHITE, (x+220*Q, y+550*Q, 60*Q, 100*Q))
     
     pygame.draw.ellipse(screen, WHITE, (x+320*Q, y+560*Q, 60*Q, 100*Q)) #1foot
     pygame.draw.ellipse(screen, WHITE, (x+330*Q, y+640*Q, 40*Q, 60*Q))
     pygame.draw.rect(screen, WHITE, (x+290*Q, y+670*Q, 20*Q, 60*Q))
     pygame.draw.polygon(screen, WHITE, [[x+310*Q, y+710*Q], [x+310*Q, y+730*Q], [x+330*Q, y+730*Q]])

     pygame.draw.ellipse(screen, WHITE, (x+280*Q, y+570*Q, 40*Q, 60*Q)) #2foot
     pygame.draw.ellipse(screen, WHITE, (x+280*Q, y+620*Q, 40*Q, 60*Q))
     pygame.draw.rect(screen, WHITE, (x+340*Q, y+690*Q, 20*Q, 60*Q))
     pygame.draw.polygon(screen, WHITE, [[x+360*Q, y+730*Q], [x+360*Q, y+750*Q], [x+390*Q, y+750*Q]])

#задние ноги
#1
     pygame.draw.polygon(screen, WHITE, [[x+190*Q, y+610*Q], [x+210*Q, y+610*Q], [x+210*Q, y+730*Q], [x+190*Q, y+730*Q]])
     pygame.draw.polygon(screen, WHITE, [[x+190*Q, y+610*Q], [x+210*Q, y+610*Q], [x+210*Q, y+730*Q], [x+190*Q, y+730*Q]])
     pygame.draw.polygon(screen, WHITE, [[x+240*Q, y+610*Q], [x+255*Q, y+610*Q], [x+255*Q, y+720*Q], [x+240*Q, y+720*Q]])
#2 
     pygame.draw.polygon(screen, WHITE, [[x+255*Q, y+705*Q], [x+270*Q, y+720*Q], [x+255*Q, y+720*Q]])
     pygame.draw.circle(screen, WHITE, (x+200*Q, y+730*Q), 10*Q)
     pygame.draw.polygon(screen, WHITE, [[x+210*Q, y+730*Q], [x+200*Q, y+740*Q], [x+230*Q, y+740*Q]])
#neck
     pygame.draw.polygon(screen, WHITE, [[x+300*Q, y+530*Q], [x+300*Q, y+350*Q], [x+350*Q, y+350*Q], [x+350*Q, y+390*Q], [x+400*Q, y+530*Q]]) 
#roga
     pygame.draw.polygon(screen, WHITE, [[x+300*Q, y+290*Q], [x+300*Q, y+350*Q], [x+330*Q, y+350*Q]]) 
     pygame.draw.polygon(screen, WHITE, [[x+330*Q, y+280*Q], [x+340*Q, y+325*Q], [x+320*Q, y+340*Q]])
#head
     pygame.draw.ellipse(screen, WHITE, (x+300*Q, y+320*Q, 100*Q, 60*Q))
     pygame.draw.ellipse(screen, WHITE, (x+350*Q, y+370*Q, 40*Q, 20*Q))
#eye
     pygame.draw.circle(screen, BLACK, (x+340*Q, y+350*Q ), 20*Q, 1)
     pygame.draw.circle(screen, BLACK, (x+350*Q, y+350*Q), 4*Q)
     pygame.draw.circle(screen, WHITE, (x+380*Q, y+330*Q), 20*Q)
     pygame.draw.circle(screen, BLACK, (x+380*Q, y+330*Q), 20*Q, 1)
     pygame.draw.circle(screen, BLACK, (x+385*Q, y+325*Q), 4*Q)


lama(300, 100,6)
lama(0, 0, 10)
lama(50,200,4)

#lama2
pygame.draw.polygon(screen, WHITE, [[800, 500], [800, 800], [690, 800]])
pygame.draw.ellipse(screen, WHITE, (680, 530, 120, 80))
pygame.draw.ellipse(screen, WHITE, (700, 590, 70, 44))
pygame.draw.polygon(screen, WHITE, [[780, 500], [750, 550], [780, 550]])
#eye
pygame.draw.circle(screen, WHITE, (710, 540 ), 20)
pygame.draw.circle(screen, BLACK, (710, 540 ), 20, 1)
pygame.draw.circle(screen, BLACK, (700, 530), 4)
pygame.draw.circle(screen, WHITE, (740, 560 ), 30) 
pygame.draw.circle(screen, BLACK, (740, 570 ), 20, 1)
pygame.draw.circle(screen, BLACK, (740, 560 ), 30, 1)
pygame.draw.circle(screen, BLACK, (735, 570 ), 5)

s = pygame.Surface((800,800))
s.fill(BLACK)
s.set_alpha(128)
s.set_colorkey(BLACK)
pygame.draw.ellipse(s, Pale, (450, 100, 360, 180))
pygame.draw.ellipse(s, DarkOrange, (50, 0, 550, 200))
screen.blit(s,(0,0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

