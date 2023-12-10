#256 by 64 buttons
# python3 squirrelrun.py

import pygame

class Button():
    def __init__(self, x, y, img):
        self.img = pygame.transform.scale(img, (int(x), int(y)))
        self.clicked = False

    def draw(self, screen, x, y, scale = None):
        #get dimentions
        if scale is not None:
            self.img = pygame.transform.scale(self.img, (int(x) * int(scale), int(y) * int(scale)))
        #create button area 
        self.rect = self.img.get_rect()
        #top left of the button area at x,y coordinates
        self.rect.topleft = (x, y)
        
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def isClicked(self):
        ## make a check to see if the button was drawn first
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            #check if button rect has a new mouse press
            #the and___ makes sure it only registers one time as clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        return False

