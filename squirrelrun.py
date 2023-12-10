import pygame, sys
import button
pygame.init()
screen = pygame.display.set_mode((1280, 720))

#Title and icon
pygame.display.set_caption("Squirrel Run")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# load and scale background
bg = pygame.image.load('assets/background.png')
bg = pygame.transform.scale(bg, (1280, 720))

# load button
start_button_image= pygame.image.load('assets/startbutton.png')
# start_button_image = pygame.image.load('assets/startbutton.png')
start_button = button.Button(256, 64, start_button_image)
#quit_button = button.Button()

def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, (0,0))
        cursor_pos = pygame.mouse.get_pos()
        start_button.draw(screen, 250, 500)
        if start_button.isClicked():
            print("start clicked")
            play()
        pygame.display.flip()

def play():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((156, 67, 181))
        pygame.display.flip()

def levels():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main_menu()
