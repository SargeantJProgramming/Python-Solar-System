from SpaceObject import SpaceObject

class Planet(SpaceObject):
  
  def __init__(self,radius,colour,coordinates,orbitSun,orbitRadius):
    self.radius = radius
    self.colour = colour
    self.coordinates = coordinates
    self.orbitRadius = orbitRadius
    self.orbitSun = orbitSun