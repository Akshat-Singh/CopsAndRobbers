import pygame


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.draw.rect(screen, (255, 0, 255), ((700, 200), (75, 75)))
pygame.draw.rect(screen, (255, 255, 0), ((950, 100), (75, 75)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()

