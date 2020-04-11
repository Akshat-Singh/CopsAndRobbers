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

# GRAPH ATTRIBUTES #
nodeVector = [pygame.sprite.Sprite() for i in range(10)]
counter = 0.5
locationVector = []
for node in nodeVector:
    node.image = pygame.transform.scale(pygame.image.load("sprites/node.png").convert_alpha(), (75, 75))
    node.rect = node.image.get_rect(center=(counter * 100, counter * 100))
    locationVector.append((counter * 100, counter * 100))
    screen.blit(node.image, node.rect)
    counter = counter + 1

# COP ATTRIBUTES #
cop = pygame.sprite.Sprite()
cop.image = pygame.transform.scale(pygame.image.load("sprites/cop.png").convert_alpha(), (45, 45))
cop.rect = cop.image.get_rect(center=locationVector[0])
screen.blit(cop.image, cop.rect)


# DRAW EDGES #
for i in range(9):
    pygame.draw.line(screen, (0, 0, 0), nodeVector[i].rect.bottomright, nodeVector[i + 1].rect.topleft, 5)



def gameplay(gameRunning):
    """ Function that controls the essential initial components of the game """
    while gameRunning:
        for userAction in pygame.event.get():
            if userAction.type == pygame.QUIT:
                gameRunning = False
        pygame.display.flip()


runStatus = True
gameplay(runStatus)
