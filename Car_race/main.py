import pygame
from pygame.locals import *

size = width, hight =(1200,800)
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

#----------Vehicle 1-------------
car = pygame.image.load("images/car.png")
car_location = car.get_rect()
car_location.center = width/2 + road_w/4 , height*0.8

#----------Vehicle 2-------------
car_2 =pygame.image.load("images/car2.png")
car2_location = car.get_rect()
car2_location.center = width/2 - road_w/4 , height*0.2



while running:
  for event in pygame.event.get()
    if event.type == QUITE:
      running = False

  screen.blit(car,car_location)
  pygame.display.update()
  screen.blit(car2,car2_location)
  pygame.display.update()

pygame.quite()
