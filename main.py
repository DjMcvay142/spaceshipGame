import pygame
from random import randint
from os.path import join

pygame.init()
window_width, window_height = 1280, 720
display_surface = pygame.display.set_mode((window_width,window_height))
running = True

# Game Title and Icon

title = "Spaceship Game"
pygame.display.set_caption(title)

# Plain Surface

Surface = pygame.Surface((100,200))
Surface.fill("orange")
x = 100

# Importing an Image
player_surface = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rect = player_surface.get_frect(center = (window_width / 2, window_height / 2))
star_surface = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0,window_width),randint(0,window_height)) for i in range(20)]

meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (window_width / 2, window_height / 2))


while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Draw the Game
    display_surface.fill("black")

    # Star Background
    for position in star_positions:
        display_surface.blit(star_surface, position)

    display_surface.blit(player_surface, player_rect)
    display_surface.blit(meteor_surface, meteor_rect)

    pygame.display.update()


pygame.quit()