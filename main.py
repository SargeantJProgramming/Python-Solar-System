import sys, pygame
from Sun import Sun
from Planet import Planet

pygame.init()

height = 400
width = 400
size = [height,width]

centre = (height/2,width/2)
space = pygame.display.set_mode(size)

mainSun = Sun(100,(10,10,10),(100,100))

planetA = Planet(300,(10,10,10),(10,10),mainSun,150)

print(planetA.orbitSun)
