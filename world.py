import pygame

tile_size = 80
class World():
    def __init__(self, data):
        ##list of image and rect (with coordinates) tuples
        self.tile_list = []
        image_one = pygame.image.load('assets/dirt.png')
        image_two = pygame.image.load('assets/grass.png')
        self.image_three = pygame.transform.scale(pygame.image.load('assets/lava.png'), (tile_size, tile_size))
        self.image_four = pygame.transform.scale(pygame.image.load('assets/portal.png'), (tile_size, tile_size))
        # y coord of each tile being placed increases as we move down
        rcount = 0
        for row in data:
            # x coord of each tile being placed increases as we move along each row
            ccount = 0
            for tile in row:
                image = pygame.transform.scale(image_one, (tile_size, tile_size))
                #maybe change below into a for loop and put the tile images in a list
                if tile == 0:
                    ccount+=1
                    continue
                
                if tile == 1:
                    image = pygame.transform.scale(image_one, (tile_size, tile_size))

                if tile == 2:
                    image = pygame.transform.scale(image_two, (tile_size, tile_size))

                if tile == 3:
                    image = self.image_three
                if tile == 4:
                    image = self.image_four
                    
                img_rect = image.get_rect()
                img_rect.x = ccount*tile_size
                img_rect.y = rcount*tile_size 
                #store this new created tile in the list
                tile_tuple = (image, img_rect)
                self.tile_list.append(tile_tuple)

                ccount +=1
            rcount+=1

    def draw(self, screen):
        for tile_tuple in self.tile_list:
            #display the tile onto the screen based on the stored image, and coordinates 
            screen.blit(tile_tuple[0], tile_tuple[1])

    #takes in a tile tuple, checks if its deadly
    def isDeadly(self, tile):
        if tile[0] is self.image_three:
            print("collided with lava")
            return True
        return False