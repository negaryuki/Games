import pygame
from pygame.locals import *

size = width, hight =(800,800)
road_w = int(width/1.6)
roadmark_w= int(width/80)

pygame.init()
running = True

#Set Window Size
screen = pygame.display.set_mode(size)

#Set Title
pygame.display.set_caption("Negar's Car game")

#Set Background colour
screen.fill((60,220,0))

#Draw graphics:
#---------Road--------------
pygame.draw.rect(
  screen,
  (50,50,50),
  (width/2 - road_w/2,0, road_w ,height)
  )

#----------Roadmark-------------
pygame.draw.rect(
  screen,
  (255,240,60),
  (width/2 - roadmark_w/2,0, roadmark_w, height)
  )
#----------Roadmark end 1-------------
pygame.draw.rect(
  screen,
  (255,255,255),
  (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height)
  )
#----------Roadmark end 2-------------
pygame.draw.rect(
  screen,
  (255,255,255),
  (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height)
  )
  

#Apply changes
pygame.display.update()

while running:
  for event in pygame.event.get()
    if event.type == QUITE:
      running = False

pygame.quite()
