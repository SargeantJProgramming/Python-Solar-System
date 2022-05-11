import sys, pygame
from SpaceObject import SpaceObject

pygame.init()

height = 400
width = 400
size = [height,width]

centre = (height/2,width/2)
space = pygame.display.set_mode(size)
#pygame.draw.circle(space,[255,200,0],centre,10)
#pygame.display.update()
#self,objectRadius, orbitCentre,orbitRadius,speed,colour 
sun = SpaceObject(10,centre,0,10,(255,200,0))
#print(sun.colour,sun.orbitCentre,sun.objectRadius)
pygame.draw.circle(space,sun.colour,sun.orbitCentre,sun.objectRadius)
pygame.display.update()

moon = SpaceObject(5,(sun.currentCoordinates[0],sun.currentCoordinates[1]),10,10,(150,150,150))

print((sun.currentCoordinates[0],sun.currentCoordinates[1]),10,10,(150,150,150))
print(moon.colour,moon.orbitCentre,moon.objectRadius)
pygame.draw.circle(space,moon.colour,moon.orbitCentre,moon.objectRadius)
pygame.display.update()
