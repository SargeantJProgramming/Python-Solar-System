import math

class SpaceObject():
  orbitCentre = (0,0)
  orbitRadius = 0
  objectRadius = 0
  speed = 0
  colour = (0,0,0)
  currentCoordinates = (0,0)
  
  def __init__(self,objectRadius, orbitCentre,orbitRadius,speed,colour):
    self.objectRadius = objectRadius
    self.orbitCentre = orbitCentre
    self.orbitRadius = orbitRadius
    self.colour = colour
    self.speed = speed

  def updateRadius(self,orbitCentre,orbitRadius):
    self.orbitCentre = orbitCentre
    self.orbitRadius = orbitRadius

  def velocity(self):
    velocity = self.speed*self.orbitRadius*math.pi
    
