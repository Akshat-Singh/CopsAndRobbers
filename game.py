""" Header files to initialize the game """
import pygame
import gameGraph
import os
import random
from tkinter import messagebox
from tkinter import *
import platform

currentOS = platform.system()
print(f"{currentOS}")

""" GAME DRIVER CODE """
level = input("Welcome to Cops and Robbers! Please enter the level (1 - 20): ")
graphFile = open("data/level"+level+".txt", "r")
fileData = graphFile.readlines()
totalVertices, totalEdges = map(int, fileData[0].split())
graph = gameGraph.Graph(totalVertices, totalEdges)
graph.acceptGraph(fileData)
gameMatrix = graph.returnDirectedAdjacencyMatrix()
algoMatrix = graph.returnUndirectedAdjacencyMatrix()


def checkLink(nodeA, nodeB):
    if algoMatrix[nodeA][nodeB] == 1:
        return True
    Tk().wm_withdraw()  # to hide the main window
    messagebox.showinfo('Node', 'Node: ' + str(nodeA) + ' is not connected to the current Robber Node')
    return False


pygame.init()  # Initialize pygame module


""" Optimizing screen resolution factor on the basis of operating system """
if currentOS == "Windows":
    factor = 0.8
elif currentOS == "Linux":
    factor = 1
elif currentOS == "Darwin":
    factor = 0.8

""" Game Window Attributes """
screenSize = (int(1500*factor), int(1000*factor))
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Cops and Robbers")
screen.fill([255, 255, 255])

""" Sprite Attributes """

# GRAPH ATTRIBUTES #
nodeVector = [pygame.sprite.Sprite() for i in range(totalVertices)]
counter = 0

# ACCEPT GRAPH FROM FILE #
locationVector = []
file = open("data/nodePos"+level+".txt", "r")
lines = file.readlines()
for line in lines:
    x, y = map(int, line.split())
    x = int(x * factor)
    y = int(y * factor)
    locationVector.append((x, y))

for node in nodeVector:
    node.image = pygame.transform.scale(pygame.image.load("sprites/node.png").convert_alpha(), (int(75*factor), int(75*factor)))
    node.rect = node.image.get_rect(center=locationVector[counter])
    screen.blit(node.image, node.rect)
    counter = counter + 1

# COP ATTRIBUTES #
copNode = 0
cop = pygame.sprite.Sprite()
cop.image = pygame.transform.scale(pygame.image.load("sprites/cop.png").convert_alpha(), (int(45*factor), int(45*factor)))

################
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# ROBBER ATTRIBUTES #
robberNode = 1
robber = pygame.sprite.Sprite()
robber.image = pygame.transform.scale(pygame.image.load("sprites/robber.png").convert_alpha(), (int(45*factor), int(45*factor)))

# DRAW EDGES #
for i in range(totalVertices):
    for j in range(totalVertices):
        if gameMatrix[i][j] == 1 and i != j:
            pygame.draw.line(screen, (0, 0, 0), nodeVector[i].rect.center, nodeVector[j].rect.center, int(5*factor))

valCorrect = int(22 * factor)


def gameplay(gameRunning):
    """ Function that controls the essential initial components of the game """
    global robberNode, copNode
    while gameRunning:

        """ UPDATE POSITIONS OF COP AND ROBBER SPRITE AT EVERY STEP """
        screen.blit(robber.image, (locationVector[robberNode][0] - valCorrect, locationVector[robberNode][1] - valCorrect))
        screen.blit(cop.image, (locationVector[copNode][0] - valCorrect, locationVector[copNode][1] - valCorrect))
        pygame.display.flip()

        """ HANDLE USER ACTION """
        for userAction in pygame.event.get():
            """ QUIT IF THE EXIT CROSS IS CLICKED """
            if userAction.type == pygame.QUIT:
                gameRunning = False

            """ HANDLING MOUSE BUTTON CLICKS """
            if pygame.mouse.get_pressed()[0]:
                for i in range(totalVertices):
                    if nodeVector[i].rect.collidepoint(pygame.mouse.get_pos()):

                        if checkLink(i, robberNode):
                            """ MOVING THE ROBBER TO A NEW NODE """
                            pygame.draw.rect(screen, (255, 0, 0), ((locationVector[robberNode][0] - valCorrect, locationVector[robberNode][1] - valCorrect),
                                             (int(45*factor), int(45*factor))))
                            robberNode = i
                            screen.blit(robber.image, (
                            locationVector[robberNode][0] - valCorrect, locationVector[robberNode][1] - valCorrect))
                            pygame.display.flip()

                            """ CHECK IF THE TWO SPRITES HAVE HIT THE SAME NODE """
                            if robberNode == copNode:
                                Tk().wm_withdraw()  # to hide the main window
                                messagebox.showinfo('Uh-Oh!', 'Looks like you were caught')
                                gameRunning = False
                                break

                            """ MOVING THE COP TO A NEW NODE """
                            pygame.draw.rect(screen, (255, 0, 0), ((locationVector[copNode][0] - valCorrect, locationVector[copNode][1] - valCorrect),
                                             (int(45 * factor), int(45 * factor))))
                            copNode = random.randint(0, 9)
                            screen.blit(cop.image, (
                                locationVector[copNode][0] - valCorrect, locationVector[copNode][1] - valCorrect))
                            pygame.display.flip()

                            """ CHECK IF THE TWO SPRITES HAVE HIT THE SAME NODE """
                            if robberNode == copNode:
                                Tk().wm_withdraw()  # to hide the main window
                                messagebox.showinfo('Uh-Oh!', 'Looks like you were caught')
                                gameRunning = False
                                break


runStatus = True
robberNode = 1
gameplay(runStatus)