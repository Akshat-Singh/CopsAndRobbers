""" Header files to initialize the game """
import pygame
import gameGraph
import os
import random
from tkinter import messagebox
from tkinter import *
import secondaries


def nodeClicked(nodeIndex):
    Tk().wm_withdraw()  # to hide the main window
    messagebox.showinfo('Node', 'Node: ' + str(nodeIndex))


def checkLink(nodeA, nodeB):
    return True




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

################
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


# ROBBER ATTRIBUTES #
robberNode = 1
robber = pygame.sprite.Sprite()
robber.image = pygame.transform.scale(pygame.image.load("sprites/robber.png").convert_alpha(), (45, 45))


# DRAW EDGES #
for i in range(9):
    pygame.draw.line(screen, (0, 0, 0), nodeVector[i].rect.bottomright, nodeVector[i + 1].rect.topleft, 5)


def gameplay(gameRunning):
    """ Function that controls the essential initial components of the game """
    global robberNode
    while gameRunning:
        screen.blit(robber.image, locationVector[robberNode])
        for userAction in pygame.event.get():
            if userAction.type == pygame.QUIT:
                gameRunning = False

            if userAction.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

            if pygame.mouse.get_pressed()[0]:
                for i in range(10):
                    if nodeVector[i].rect.collidepoint(pygame.mouse.get_pos()):
                        nodeClicked(i)
                        if checkLink(nodeVector[i], robberNode):
                            pygame.draw.rect(screen, (255, 255, 255), (locationVector[robberNode], (75, 75)))
                            robberNode = i
                            # screen.blit(pygame.get_rect, locationVector[robberNode])

        pygame.display.flip()

        pygame.display.flip()  # PyGame is double-buffered. This swaps
        # the buffers. This call is required in order for any updates
        # that we make to the game screen to become visible.


runStatus = True
robberNode = 1
gameplay(runStatus)
