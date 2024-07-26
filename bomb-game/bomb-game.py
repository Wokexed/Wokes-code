import pygame
import random
import os

# initialize pygame
pygame.init()

# parameters for game screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
CARD_WIDTH, CARD_HEIGHT = 80, 100

# set up screen display 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("18 Cards Game")

BACKGROUND_COLOR = (0, 128, 0) # green

# FPS
FPS = 60
clock = pygame.time.Clock() 

# Run until users clicks X to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

class Card:
    def __init__(self, image, position):      # initialize the objects 
        self.iamge = image 
        self.position =  position
        self.rect =  self.image.get_rect(topleft=position)
        self.is_face_up = False

    
        
 