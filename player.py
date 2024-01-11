import pygame

class Player():
    def __init__(self, img_list, x, y):
        self.img_list = img_list
        self.img = img_list[0]
        self.rect = self.img.get_rect()
        #set place of player on grid
        self.rect.x = x
        self.rect.y = y
        self.y_vel = 0
        self.jumping = False
        self.isCollided = False

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def update(self):
        x=0
        y=0
        v0 = 15

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            x-=5

        if key[pygame.K_RIGHT]:
            #pygame.transform.flip(self.img, True, False)
            x+=5

        if (key[pygame.K_SPACE] or key[pygame.K_UP]) and not self.jumping:
            #when jump, change the velocity to act against gravity. i.e., move in the opposite direction
            #this moves the players position up
            self.y_vel = -v0
            self.jumping = True
            self.img = self.img_list[1]
        
        else:
            self.jumping = False
            if self.y_vel == 0:
                self.img = self.img_list[0]
              
        #gravity; keep increasing the y velocity (accelerate downwards), until it reaches max vel (if it gets to more than v0, 
        #then our jumping will not move the player in the upwards direction unless we rapidly click jump)
        self.y_vel += 1
        if self.y_vel > v0:
            self.y_vel = v0
        
        #every tick, the players y position increases by the velocity (constant motion)
        y += self.y_vel

        #check for collisions

        #update player
        self.rect.x += x
        self.rect.y += y

        if self.rect.bottom > 640:
            self.rect.bottom = 640
            y=0

        if self.rect.top < 0:
            self.rect.top = 0

    def animate(self):
        walking_list = []