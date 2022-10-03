# import libraries
import pygame

#Initialize pygame

#window size
screen_width = 500
screen_height = 400

# size variable
size = (screen_width, screen_height)

# display the windows 
screen = pygame.display.set_mode(size)

# Game loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False