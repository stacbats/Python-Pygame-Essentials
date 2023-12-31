import pygame, sys, random              # importing important events & variables into pygame his helps us write more readable code
import pygame.locals as GAME_GLOBALS    # these wil lhelp in us creating a game state 
import pygame.event as GAME_EVENTS      # these help with keyboard & system events

pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')
while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (255,0,0), (random.randint(0, windowWidth), random.randint(0, windowHeight), 10, 10))

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()