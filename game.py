""" Header files to initialize the game """
import pygame
import gameGraph

pygame.init()       # Initialize pygame module


def gameWindow():
    """ Definition of a function to initialize the dimensions of the game window """
    screenSize = (800, 720)
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption("Cops and Robbers")  


def gameplay(gameRunning):
    """ Function that controls the essential initial components of the game """
    while gameRunning:
        for userAction in pygame.event.get():
            if userAction.type == pygame.QUIT:
                gameRunning = False


if __name__ == '__main__':
    runStatus = True
    gameWindow()
    gameplay(runStatus)

