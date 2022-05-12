import sys, pygame, time
from Sun import Sun
from Planet import Planet

pygame.init()

def drawObject(object):
  pygame.draw.circle(space,object.colour,object.coordinates,object.radius)
  pygame.display.update()

def updateObject(object):
  pygame.draw.circle(space,(0,0,0),object.oldCoordinates,object.radius)
  pygame.draw.circle(space,object.colour,object.coordinates,object.radius)
  pygame.display.update()

height = 400
width = 400
size = [height,width]

centre = (height/2,width/2)
space = pygame.display.set_mode(size)

mainSun = Sun(50,(200,150,0),centre)

planetA = Planet(20,(100,100,100),mainSun,150)

planetB = Planet(5,(100,100,100),planetA,50)


print(planetA.coordinates)
drawObject(mainSun)
updateObject(planetA)

while True: 
  print("Rotation")
  planetA.updateAngle(0.1)
  print(planetA.coordinates)
  updateObject(planetA)

  planetB.updateAngle(0.2)
  updateObject(planetB)
  
  time.sleep(0.1)