""" Header files to initialize the game """
import pygame
import gameGraph

pygame.init()  # Initialize pygame module
surface = pygame.Surface((100, 100))

""" Game Window Attributes """
screenSize = (1500, 1000)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Cops and Robbers")
screen.fill([255, 255, 255])

""" Sprite Attributes """

# COP ATTRIBUTES #
cop = pygame.sprite.Sprite()
cop.image = pygame.transform.scale(pygame.image.load("sprites/cop.png").convert_alpha(), (50, 50))
cop.rect = cop.image.get_rect(center=(75, 75))
screen.blit(cop.image, cop.rect)

# GRAPH ATTRIBUTES #
nodeVector = [pygame.sprite.Sprite() for i in range(10)]
counter = 1
for node in nodeVector:
    node.image = pygame.transform.scale(pygame.image.load("sprites/node.png").convert_alpha(), (75, 75))
    node.rect = node.image.get_rect(center=(counter * 75, counter * 75))
    screen.blit(node.image, node.rect)
    counter = counter + 1

"""
graphNode = pygame.sprite.Sprite()
graphNode.image = pygame.transform.scale(pygame.image.load("sprites/node.png").convert_alpha(), (50, 50))
graphNode.rect = graphNode.image.get_rect()
screen.blit(graphNode.image, graphNode.rect)
"""


def gameplay(gameRunning):
    """ Function that controls the essential initial components of the game """
    while gameRunning:
        for userAction in pygame.event.get():
            if userAction.type == pygame.QUIT:
                gameRunning = False
        pygame.display.flip()


runStatus = True
gameplay(runStatus)
