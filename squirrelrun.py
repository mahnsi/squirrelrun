import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

#Title and icon
pygame.display.set_caption("Squirrel Run")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

def play():
    screen.fill("black")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
