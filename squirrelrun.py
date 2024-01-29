import pygame
import button, world, player, worlddata, math
pygame.init()

screen = pygame.display.set_mode((1280, 720))
FPS = 60
numlevels = 5
#level=1
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
main_menu_button_image = pygame.image.load('assets/mainmenubutton.png')
presstostart_image = pygame.transform.scale(pygame.image.load('assets/presstostart.png'),(300, 120))
winner_image = pygame.transform.scale(pygame.image.load('assets/winner.png'),(300, 120))
start_button = button.Button(256, 64, start_button_image)
quit_button = button.Button(256, 64, quit_button_image)
main_menu_button = button.Button(256, 64, main_menu_button_image)
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

def play(data, level):
    #create world and player based on level data
    wrld = world.World(data)
    plyr = player.Player(player_list, 10, 490)
    #scale image proportional to tile size
    plyr.img = pygame.transform.scale(plyr.img, (math.floor(wrld.tile_size*1.3), math.floor(wrld.tile_size*1.4625)))
    plyr.rect = plyr.img.get_rect()
    
    clock = pygame.time.Clock()

    running = True
    start = False
    while running:
        plyr.img = pygame.transform.scale(plyr.img, (math.floor(wrld.tile_size*1.3), math.floor(wrld.tile_size*1.4625)))
        clock.tick(FPS)
        screen.blit(bg_g, (0,0))  
        back_button.draw(screen, 50, 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if back_button.isClicked():
            print("back clicked")
            start = True
            return True
        
        if not start:
            screen.blit(presstostart_image, (40, 300)) 
        
        #draw the map weve created onto the screen
        wrld.draw(screen)
        plyr.draw(screen)

        key = pygame.key.get_pressed()
        if(key[pygame.K_RETURN]):
            print("game start")
            start = True

        if start:
            if(plyr.update(wrld)==1):
                level+=1
                plyr.rect.x=0
                plyr.rect.y=560
                if len(worlddata.data_list)>level:
                    world_data = worlddata.data_list[level]
                else:
                    running = end()
                wrld = world.World(world_data)
                
        
        pygame.display.flip()

def level_select():
    button_list = []
    screen.fill((164, 237, 171))
    back_button.draw(screen, 50, 50)
    running = True

    for i in range (0, numlevels):
        button_list.append(button.Button(80, 80, level_image_list[i]))

    while running:
        j=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        if back_button.isClicked():
            print("back clicked")
            return True
            
        screen.blit(pygame.transform.scale(pygame.image.load('assets/lvl_select_text.png'), (400, 160)), (440, 50))

        for i in range(0, numlevels):
            button_list[i].draw(screen, 150 + j, 210)
            j+=100
            if button_list[i].isClicked():
                print("level " + str(i+1) + " selected")
                #change world data based on i
                world_data=worlddata.data_list[i]
                running = play(world_data, i)

        pygame.display.flip()      

def end():
    screen.fill((90,23,80))
    running = True
    while running:
        screen.blit(winner_image, (490, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        main_menu_button.draw(screen, 250, 500)
        quit_button.draw(screen, 750, 500)

        if quit_button.isClicked():
            running=False

        if main_menu_button.isClicked():
            running=main_menu()
        pygame.display.flip()


main_menu()