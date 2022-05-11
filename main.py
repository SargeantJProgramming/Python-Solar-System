import sys, pygame

pygame.init()

height = 400
width = 400
size = [height,width]

centre = [height/2,width/2]
space = pygame.display.set_mode(size)
pygame.draw.circle(space,[255,200,0],centre,10)
pygame.display.update()


