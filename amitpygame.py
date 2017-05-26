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


              

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEMOTION:
            print("'mouse at:",event.pos)
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
##            print("you pressed the mouse at",event.pos)
##            pygame.draw.line(screen,red,(event.pos),(100,900))
##            pygame.draw.line(screen,red,(100,100),(event.pos))
##            pygame.display.update()
            x,y=event.pos
            a= x -50
            b=y-50
            c=x+50
            d=y+50
            e= x +50
            f=y+50
            g=x-50
            h=y-50
            pygame.draw.line(screen,red,(a,b),(c,d))
            pygame.draw.line(screen,red,(e,h),(g,f))
            pygame.display.update()
            
        elif event.type==pygame.MOUSEBUTTONUP and event.button==1:
            print("you released the mouse at",event.pos)
            
    pygame.draw.line(screen,red,(300,0),(300,900))
    pygame.draw.line(screen,red,(600,0),(600,900))
    pygame.draw.line(screen,red,(0,300),(900,300))
    pygame.draw.line(screen,red,(0,600),(900,600))
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
