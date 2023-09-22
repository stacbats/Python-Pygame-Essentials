import pygame   # this tells us that we want to use pygame

pygame.init()   # Basically saying we are ready to use it

window = pygame.display.set_mode((500, 400)) # this one is setting up the display, the height and width 500 wide and 400 tall -500,400.
# the brackets above form a TUPLE (a list of things for this function)
while True:
    pygame.draw.rect(window,(255, 0, 0), (0, 0, 50, 30))
    pygame.display.update()


# caution running this, it has no quit function include :)