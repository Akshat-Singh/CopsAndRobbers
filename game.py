""" Header files to initialize the game """
import pygame
import gameGraph

pygame.init()  # Initialize pygame module
surface = pygame.Surface((100, 100))


""" Game Window Attributes """
screenSize = (800, 720)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Cops and Robbers")
screen.fill([255, 255, 0])

""" Sprite Attributes """

# COP ATTRIBUTES #
cop = pygame.sprite.Sprite()
cop.image = pygame.transform.scale(pygame.image.load("sprites/cop.png").convert_alpha(), (50, 50))
cop.rect = cop.image.get_rect()
screen.blit(cop.image, cop.rect)


def gameplay(gameRunning):
    """ Function that controls the essential initial components of the game """
    while gameRunning:
        for userAction in pygame.event.get():
            if userAction.type == pygame.QUIT:
                gameRunning = False
        pygame.display.flip()


runStatus = True
gameplay(runStatus)
