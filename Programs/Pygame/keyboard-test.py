import pygame, time
from pygame.locals import *

directions = {
    119: 'up',    ## w
     97: 'left',  ## a
    115: 'down',  ## s
    100: 'right', ## d
}

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(0)
pygame.key.set_repeat(1,1)

keepGoing = True
while keepGoing:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in directions:
                print("Go %s" % directions[event.key])

            if event.key == 27:
                keepGoing = False

    time.sleep(0.1)
    
pygame.quit()
