import pygame
import button, world, player, worlddata
pygame.init()

screen = pygame.display.set_mode((1280, 720))
FPS = 60
numlevels = 3
level=1
#16 tiles by 9 tiles. each tile 80 px sq

#set Title and icon
pygame.display.set_caption("Squirrel Run")
icon=pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# load and scale background
bg = pygame.image.load('assets/background.png')
bg = pygame.transform.scale(bg, (1280, 720))
bg_g = pygame.transform.scale(pygame.image.load('assets/background.png'), (1280, 720))


# load button images and buttons - start, quit, back, lvl
start_button_image= pygame.image.load('assets/startbutton.png')
quit_button_image= pygame.image.load('assets/quitbutton.png')
back_button_image = pygame.image.load('assets/backbutton.png')
start_button = button.Button(256, 64, start_button_image)
quit_button = button.Button(256, 64, quit_button_image)
back_button = button.Button(75, 75, back_button_image)

level_image_list = []
for i in range (1, numlevels+1):
    path = f'assets/Lpics/L{i}.png'
    level_image_list.append(pygame.image.load(path))

#load player imagess ---> 150,150 are the dimentions
player_image = pygame.transform.scale(pygame.image.load('assets/squirrelmain.png'), (104,117))
player_jumping = pygame.transform.scale(pygame.image.load('assets/squirreljump.png'), (104,117))
player_reverse = pygame.transform.scale(pygame.image.load('assets/squirrelmain_reverse.png'), (104,117))
player_list = [player_image, player_jumping, player_reverse]

world_data = worlddata.l1
plyr = player.Player(player_list, 10, 490)

def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, (0,0))
        screen.blit(pygame.transform.scale(pygame.image.load('assets/title_text.png'), (900, 120)), (190, 150))

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
    start = False
    while running:
        clock.tick(FPS)
        screen.blit(bg_g, (0,0))
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
        
        key = pygame.key.get_pressed()
        if(key[pygame.K_RETURN]):
            print("game start")
            start = True

        if start:
            plyr.update(wrld)
        

        pygame.display.flip()

def level_select():
    j=0
    button_list = []
    screen.fill((164, 237, 171))
    back_button.draw(screen, 50, 50)
    running = True

    screen.blit(pygame.transform.scale(pygame.image.load('assets/lvl_select_text.png'), (400, 160)), (440, 50))
    for i in range (0, numlevels):
        button_list.append(button.Button(80, 80, level_image_list[i]))
        button_list[i].draw(screen, 150 + j, 210)
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
                level = i
                running = play(world_data)

        pygame.display.flip()


def gameOver():
    print("lost")
    plyr.rect.x = 0
    plyr.rect.y = 560
        
def win():
    print("win")
    world_data=worlddata.data_list[level+1]
    #play(world_data)

main_menu()