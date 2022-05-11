class SpaceObject():
  orbitCentre = [0,0]
  orbitRadius = 0
  objectRadius = 0
  speed = 0
  
  def __init__(self,objectRadius, orbitCentre,orbitRadius,speed):
    self.objectRadius = objectRadius
    self.orbitCentre = orbitCentre
    self.orbitRadius = orbitRadius
    self.speed = speed

  def updateRadius(self,orbitCentre,orbitRadius):
    self.orbitCentre = orbitCentre
    self.orbitRadius = orbitRadius

    
