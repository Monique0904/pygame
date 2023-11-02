
import pygame
import random


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Prog Fundamentals")

x_cord = 500
y_cord = 300

running = True

while running == True:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (x_cord, y_cord, 50, 50))

    if event.type == pygame.QUIT:
        break

    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:

        x_cord -= 1

    if button[pygame.K_RIGHT]:

        x_cord += 1

    if button[pygame.K_UP]:

        y_cord -= 1

    if button[pygame.K_DOWN]:

        y_cord += 1

    if x_cord < 0:
        x_cord = 0

    pygame.time.Clock().tick(60)

    pygame.display.flip()