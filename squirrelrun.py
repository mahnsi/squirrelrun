import pygame, sys
import button, world, player, worlddata
pygame.init()
screen = pygame.display.set_mode((1280, 720))
FPS = 60
numlevels = 2
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

level_image_list = []
for i in range (1, numlevels+1):
    path = f'assets/L{i}.png'
    level_image_list.append(pygame.image.load(path))

#load player images ---> 150,150 are the dimentions
player_image = pygame.transform.scale(pygame.image.load('assets/lava.png'), (150,150))
player_jumping = pygame.transform.scale(pygame.image.load('assets/lava.png'), (150,150))
player_list = [player_image, player_jumping]

world_data = worlddata.l1
plyr = player.Player(player_list, 0, 560)

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

def play(data):

    wrld = world.World(data)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        screen.blit(bg, (0,0))
        back_button.draw(screen, 50, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if back_button.isClicked():
            print("back clicked")
            return True
        
        #draw the map weve created onto the screen
        wrld.draw(screen)
        plyr.draw(screen)
        
        for tile in wrld.tile_list:
            if tile[1].colliderect(plyr.rect):
                if wrld.isDeadly(tile):
                    gameOver()
                if tile[0] is wrld.image_four:
                    win()
                if plyr.y_vel < 0:
                    plyr.rect.y = tile[1].bottom
                    plyr.y_vel = 0

                elif plyr.y_vel >= 0:
                    #print(player.rect.right, tile[1].left)
                    if ((plyr.rect.right - tile[1].left) == 5):
                        plyr.rect.x = tile[1].left - plyr.rect.width
                    
                    elif((plyr.rect.left - tile[1].right) == -5):
                        plyr.rect.x = tile[1].right

                    else:
                        plyr.rect.y = tile[1].top - plyr.rect.height
                        plyr.y_vel = 0


        plyr.update()
        pygame.display.flip()

def level_select():
    j=0
    button_list = []
    screen.fill((156, 107, 81))
    back_button.draw(screen, 50, 50)
    running = True

    for i in range (0, numlevels):
        button_list.append(button.Button(80, 80, level_image_list[i]))
        button_list[i].draw(screen, 150 + j, 150)
        j+=100

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if back_button.isClicked():
            print("back clicked")
            return True
        
        for i in range(0, numlevels):
            if button_list[i].isClicked():
                print("level " + str(i+1) + " selected")
                #change world data based on i
                world_data=worlddata.data_list[i]
                running = play(world_data)

        pygame.display.flip()


def gameOver():
    print("lost")
    plyr.rect.x = 0
    plyr.rect.y = 560
        
def win():
    print("win")

main_menu()