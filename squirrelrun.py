import pygame, sys
import button, world, player
pygame.init()
screen = pygame.display.set_mode((1280, 720))
FPS = 60
#16 tiles by 9 tiles. each tile 80 px sq
#python3 squirrelrun.py

#set Title and icon
pygame.display.set_caption("Squirrel Run")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# load and scale background
bg = pygame.image.load('assets/background.png')
bg = pygame.transform.scale(bg, (1280, 720))

# load button images and buttons - start, quit, back, lvl
start_button_image= pygame.image.load('assets/startbutton.png')
quit_button_image= pygame.image.load('assets/quitbutton.png')
back_button_image = pygame.image.load('assets/backbutton.png')
start_button = button.Button(256, 64, start_button_image)
quit_button = button.Button(256, 64, quit_button_image)
back_button = button.Button(75, 75, back_button_image)
level_button = button.Button(80, 80, back_button_image)

#load player images ---> 150,150 are the dimentions
player_image = pygame.transform.scale(pygame.image.load('assets/lava.png'), (150,150))
player_jumping = pygame.transform.scale(pygame.image.load('assets/lava.png'), (150,150))
player_list = [player_image, player_jumping]


world_data =[
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0],
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

world = world.World(world_data)
player = player.Player(player_list, 0, 560)

def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, (0,0))
        cursor_pos = pygame.mouse.get_pos()
        start_button.draw(screen, 250, 500)
        quit_button.draw(screen, 750, 500)

        if start_button.isClicked():
            print("start clicked")
            running = level_select()

        if quit_button.isClicked():
            running=False

        pygame.display.flip()

def play():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        screen.blit(bg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #draw the map weve created onto the screen
        world.draw(screen)
        player.draw(screen)
        
        for tile in world.tile_list:
            if tile[1].colliderect(player.rect):
                if world.isDeadly(tile):
                    gameOver()
                if tile[0] is world.image_four:
                    win()
                if player.y_vel < 0:
                    print("collided from under")
                    player.rect.y = tile[1].bottom
                    player.y_vel = 0

                elif player.y_vel >= 0:
                    #print(player.rect.right, tile[1].left)
                    if ((player.rect.right - tile[1].left) == 5):
                        print("collided from left")
                        player.rect.x = tile[1].left - player.rect.width
                    
                    elif((player.rect.left - tile[1].right) == -5):
                        print("collided from right")
                        player.rect.x = tile[1].right

                    else:
                        print("collided from top")
                        player.rect.y = tile[1].top - player.rect.height
                        player.y_vel = 0


        player.update()
        pygame.display.flip()

def level_select():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        screen.fill((156, 107, 81))
        back_button.draw(screen, 50, 50)
        level_button.draw(screen, 150, 150)
        if back_button.isClicked():
            print("back clicked")
            return True
        
        if level_button.isClicked():
            print("level selected")
            running = play()
        pygame.display.flip()


def gameOver():
    print("lost")
    player.rect.x = 0
    player.rect.y = 560
        
def win():
    print("win")

main_menu()