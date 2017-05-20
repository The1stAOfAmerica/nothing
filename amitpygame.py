from pygame.locals import*
import time
import pygame
green=(0,255,0)
blue=(0,0,255)
red=(255,0,0)
pygame.init()
a=1
pointy=[(100,0),(0,200),(300,200)]
screen=pygame.display.set_mode((900,900))
pygame.display.set_caption("Please Hold. We Will Be With You In A Couple Of Minutes*Beep*")

##pygame.draw.circle(screen,blue,(440,440),100,10)
##pygame.draw.circle(screen,green,(430,430),100,10)
##pygame.draw.circle(screen,blue,(420,420),100,10)
##pygame.draw.circle(screen,green,(410,410),100,10)
##pygame.draw.circle(screen,blue,(400,400),100,10)
##pygame.draw.circle(screen,green,(460,460),100,10)
##pygame.draw.circle(screen,blue,(470,470),100,10)
##pygame.draw.circle(screen,green,(480,480),100,10)
##pygame.draw.circle(screen,blue,(490,490),100,10)
##pygame.draw.circle(screen,green,(500,500),100,10)
##pygame.draw.circle(screen,green,(510,510),100,10)
##pygame.draw.rect(screen,red,(200,200,800,400),10)
##pygame.draw.polygon(screen,blue,pointy,10)
##pygame.draw.circle(screen,blue,(120,100),50,40)
def makeymakey():
    pygame.draw.line(screen,red,(900,100),(100,900))
    pygame.draw.line(screen,red,(100,100),(900,900))
    pygame.display.update()

makeymakey()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEMOTION:
            print("'mouse at:",event.pos)
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            print("you pressed the mouse at",event.pos)
            
        elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
            print("you released the mouse at",event.pos)
##
##while True:
##    a=a+1
##    pygame.draw.circle(screen,red,(450,450),a,1)
##    print(a)
##    time.sleep(0.000001)
##    pygame.display.update()
##    if a==450:
##        while True:
##            screen.fill((0,0,0))
##            a=a-1
##            if a==2:
##                screen.fill((0,0,0))
##                pygame.display.update()
##                quit()
##            pygame.draw.circle(screen,red,(450,450),a,1)
##            print(a)
##            time.sleep(0.000001)
##            pygame.display.update()
##
