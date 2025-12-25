import pygame
from random import randint
from os.path import join

pygame.init()
window_width, window_height = 1280, 720
display_surface = pygame.display.set_mode((window_width,window_height))
running = True
clock = pygame.time.Clock()

# Game Title and Icon

title = "Spaceship Game"
pygame.display.set_caption(title)

# Plain Surface

Surface = pygame.Surface((100,200))
Surface.fill("orange")
x = 100

# Imports
player_surface = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rect = player_surface.get_frect(center = (window_width / 2, window_height / 2))
player_direction = 1

star_surface = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0,window_width),randint(0,window_height)) for i in range(20)]

meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (window_width / 2, window_height / 2))

laser_surface = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surface.get_rect(bottomleft = (20, window_height - 20))


while running:

    clock.tick()

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Draw the Game
    display_surface.fill("black")

    # Star Background
    for position in star_positions:
        display_surface.blit(star_surface, position)

    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)



    # Player Movement
    player_rect.x += 20
    player_rect.y -= 10
    display_surface.blit(player_surface, player_rect)


    pygame.display.update()


pygame.quit()