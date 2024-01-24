import pygame
from pygame import mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

#load sounds
jump_sound = pygame.mixer.Sound('assets/sounds/jump.wav')
gameover_sound = pygame.mixer.Sound('assets/sounds/gameover.wav')
win_sound = pygame.mixer.Sound('assets/sounds/win.wav')
win_sound.set_volume(0.2)

class Player():
    def __init__(self, img_list, x, y):
        self.img_list = img_list
        self.img = img_list[0]
        self.rect = self.img.get_rect()
        #set place of player on grid
        self.rect.x = x
        self.rect.y = y
        self.gravity = 1
        self.y_vel = 0
        self.jumping = False
        self.isCollided = False
        self.dx = 0
        self.dy = 0

    def draw(self, screen, pos = None):
        if pos is not None:
            screen.blit(self.img, (pos[0], pos[1]))
        else:
            screen.blit(self.img, self.rect)
        #pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

    def update(self, wrld):
        self.dx=0
        self.dy = 0
        v0 = 15

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.dx-=5
            self.img = self.img_list[2]

        if key[pygame.K_RIGHT]:
            #pygame.transform.flip(self.img, True, False)
            self.dx+=5

        if ((key[pygame.K_SPACE] or key[pygame.K_UP]) and not self.jumping):
            jump_sound.play()
            self.y_vel = -19
            self.jumping = True
            self.img = self.img_list[1]
            print("jump")

        if((key[pygame.K_SPACE] == False) and (key[pygame.K_UP]==False)):
            self.jumping = False
            self.img = self.img_list[0]

        #gravity
        self.y_vel += self.gravity
        #limit on the speed of gravity (terminal velocity)
        if self.y_vel > 10:
                self.y_vel = 10

        #always acting
        self.dy += self.y_vel

        for tile in wrld.tile_list:
            if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.rect.width, self.rect.height):
                self.dx = 0
                if tile[0] is wrld.image_four: #image four is the portal
                    win_sound.play()
                    print("win")
                    #win()

            #if player is about to collide with a tile
            if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height): 
                if wrld.isDeadly(tile):
                    gameover_sound.play()
                    print("lose")
                    self.rect.y = 560
                    self.rect.x = 0
                    '''
                    for i in range (0,5):
                        if (i%2 == 0):
                            self.rect.x = 0
                        elif(i%2 == 1):
                            self.rect.x = -60
                        pygame.display.flip()
                        pygame.time.delay(300)
                    '''

                #collide from below block
                if self.y_vel < 0:
                    self.dy = tile[1].bottom - self.rect.top
                    self.y_vel = 0

                #still or falling
                elif self.y_vel >= 0: #still or falling
                    self.dy = tile[1].top - self.rect.bottom
                    self.y_vel = 0

        if (self.rect.x<0):
            self.rect.x = 0

        if(self.rect.right>1280):
            self.rect.right = 1280

        self.rect.x += self.dx
        self.rect.y += self.dy
        
    def animate(self):
        walking_list = []