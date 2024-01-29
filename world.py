import pygame, enemy

class World():

    def __init__(self, data):
        self.tile_size = 720 / len(data)
        ##list of image and rect (with coordinates) tuples
        self.tile_list = []
        image_one = pygame.image.load('assets/dirt.png')
        image_two = pygame.image.load('assets/grass.png')
        image_three = pygame.transform.scale(pygame.image.load('assets/lava.png'), (self.tile_size, self.tile_size)) 
        
        self.owl_group = pygame.sprite.Group()
        self.portal_group = pygame.sprite.Group()
        self.hazard_group = pygame.sprite.Group()
        self.movingplatform_group = pygame.sprite.Group()

        self.collidables = []
        # y coord of each tile being placed increases as we move down
        rcount = 0
        for row in data:
            # x coord of each tile being placed increases as we move along each row
            ccount = 0
            for tile in row:
                image = pygame.transform.scale(image_one, (self.tile_size, self.tile_size))
                #maybe change below into a for loop and put the tile images in a list
                if tile == 0:
                    ccount+=1
                    continue            
                if tile == 1:
                    image = pygame.transform.scale(image_one, (self.tile_size, self.tile_size))
                if tile == 2:
                    image = pygame.transform.scale(image_two, (self.tile_size, self.tile_size))
                if tile == 3:
                    image = pygame.transform.scale(image_three, (self.tile_size, self.tile_size))
                    hazard = Hazard(ccount*self.tile_size, (rcount*self.tile_size), image)
                    self.hazard_group.add(hazard)
                    ccount+=1
                    continue
                if tile == 4:
                    portal = Portal(ccount*self.tile_size, (rcount*self.tile_size)-(self.tile_size//2))
                    self.portal_group.add(portal)
                    ccount+=1
                    continue
                if tile == 5:
                    owl = Enemy(ccount*self.tile_size, (rcount*self.tile_size)+20)
                    self.owl_group.add(owl)
                    ccount+=1
                    continue
                if tile == 6:
                    movingplatform = MovingPlatform(ccount*self.tile_size, (rcount*self.tile_size), self.tile_size)
                    self.movingplatform_group.add(movingplatform)
                    self.collidables.append(movingplatform.rect)
                    ccount+=1
                    continue

                    
                img_rect = image.get_rect()
            
                img_rect.x = ccount*self.tile_size
                img_rect.bottom = (rcount + 1)*self.tile_size 

                #store this new created tile in the list
                tile_tuple = (image, img_rect)
                self.collidables.append(img_rect)
                self.tile_list.append(tile_tuple)

                ccount +=1
            rcount+=1

    def draw(self, screen):
        for tile_tuple in self.tile_list:
            #display the tile onto the screen based on the stored image, and coordinates 
            screen.blit(tile_tuple[0], tile_tuple[1])
        self.owl_group.draw(screen)
        self.owl_group.update()

        self.portal_group.draw(screen)
        self.hazard_group.draw(screen)

        self.movingplatform_group.draw(screen)
        self.movingplatform_group.update()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/owl.png'), (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter +=1 
        if abs(self.move_counter) > 60:
            self.move_direction *= -1
            self.move_counter *= -1
    
class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/portal.png'), (80, 80*1.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Hazard(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class MovingPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/grass.png'), (tile_size, tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter +=1 
        if abs(self.move_counter) > 60:
            self.move_direction *= -1
            self.move_counter *= -1