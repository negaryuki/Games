import pygame
from pygame.locals import *
import random

#----------Constants-------------
size = width, hight =(1200,800)
road_w = int(width/1.6)
roadmark_w= int(width/80)
right_lane = width/2 + road_w/4 
left_lane= width/2 - road_w/4
speed= 1

pygame.init()
running = True

#Set Window Size
screen = pygame.display.set_mode(size)

#Set Title
pygame.display.set_caption("Negar's Car game")

#Set Background colour
screen.fill((60,220,0))

# apply changes
pygame.display.update()

#----------Vehicle 1-------------
car = pygame.image.load("images/car.png")
car_location = car.get_rect()
car_location.center = right_lane, height*0.8

#----------Vehicle 2-------------
car_2 =pygame.image.load("images/car2.png")
car2_location = car.get_rect()
car2_location.center = left_lane, height*0.2  
  
counter = 0

while running:
  counter +=1
  
#--------game difficulty-----------
  if counter== 5000:
    speed += 0.15
    counter = 0
    print("level up", speed)

#--------Animate Enemy Car-----------    
    car2_location[1]+= speed 
    if car2_location > height:
      if random.randint(0,1) ==0:
        car2_location = right_lane, -200
      else:
        car2_location = left_lane, - 200  
    
#--------End game Logic-----------    
    if car_location[0] == car2_location[0] and car2_location[1] > car_location[1]-250
      print("GAME OVER")
      break
          
#--------Event Listener-----------
  for event in pygame.event.get()    
    if event.type == QUITE:
      running = False
      
    if event.type =KEYDOWN:
      if event.key in [K_a, K_LEFT]
        car_location = car_location.move([-int(road_w/2), 0])
          
      if event.key in [K_d, K_RIGHT]
        car_location = car_location.move([int(road_w/2), 0])
        
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
               
#----------Place Images------------
  screen.blit(car,car_location)
  screen.blit(car2,car2_location)
  
#Apply changes
  pygame.display.update()

pygame.quite()

#Special Thanks to Mariya for the wonderful Tutorial 
