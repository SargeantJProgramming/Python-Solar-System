import math
from SpaceObject import SpaceObject

class Planet(SpaceObject):

  coordinates = (0,0)
  angle = 0
  oldCoordinates = (0,0)
  def __init__(self,radius,colour,orbitSun,orbitRadius):
    self.radius = radius
    self.colour = colour
    self.orbitRadius = orbitRadius
    self.orbitSun = orbitSun
    self.coordinates = (orbitSun.coordinates[0] + orbitRadius*math.cos(self.angle),orbitSun.coordinates[1] + orbitRadius*math.sin(self.angle))


  def updateAngle(self,velocity):
    print(self.angle)
    self.angle = self.angle + (1*velocity)
    self.oldCoordinates = self.coordinates
    self.coordinates = (self.orbitSun.coordinates[0] + self.orbitRadius*math.cos(self.angle),self.orbitSun.coordinates[1] + self.orbitRadius*math.sin(self.angle))


