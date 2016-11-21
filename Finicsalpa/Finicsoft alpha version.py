import random
import pygame
import time
pygame.init()
display_x=800
display_y=600
y1=0
score=0
crashdep=15
appdisplay=pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('finics Game')
black = (0,0,0)
white = (255,255,255)
x1=random.randrange(0,display_x)

clock=pygame.time.Clock()
dude=pygame.image.load('Dude2.png')



    



gameExit=False
x_change=0
y_change=0
x=display_x*.45
y=display_y*.8
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_x/2),(display_y/2))
    appdisplay.blit(TextSurf, TextRect)


def fun(x,y):
  appdisplay.blit(dude,(x,y))
def crash():
    message_display('Your are Crashed')
    
def things(x1,y1):
    pygame.draw.rect(appdisplay,black,[x1,y1,150,150])
    
while not gameExit:
  for event in pygame.event.get():
    
    if event.type==pygame.QUIT:
        gameExit=True
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
             x_change+=5
        elif event.key==pygame.K_LEFT:
             x_change+=-5
        
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            x_change=0
            y_change=0
    
            
  x+=x_change
  y+=y_change
  y1+=crashdep
  appdisplay.fill(white)
  fun(x,y)
  things(x1,y1)     
  

    
  if x>display_x-73 or x<0:
      x_change=0
      crashdep=0
      crash()
      
  if y-150<y1:
      if x>x1 and x<x1+150:
          crashdep=0
          crash()
          
  if y<0 or y>display_y-70:
      y_change=0
      
      
  if y1>display_y:
      score=score=+1
      y1=-50
      x1=random.randrange(0,display_x)
  
  

  pygame.display.update()
  clock.tick(60)
pygame.quit()
quit()
