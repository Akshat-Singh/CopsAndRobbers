import pygame
import gameGraph
import random
import os


WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
#player_img = pygame.image.load(os.path.join(img_folder, 'robber.jpeg')).convert()


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.image.load(os.path.join(img_folder, "robber1.png")).convert()

        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (WIDTH / 2, HEIGHT / 2)




# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robber")
clock = pygame.time.Clock()


all_sprites.draw(screen)
# *after* drawing everything, flip the display
pygame.display.flip()

pygame.quit()
