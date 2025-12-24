import pygame
from os.path import join

pygame.init()
windowWidth, windowHeight = 1280, 720
display_surface = pygame.display.set_mode((windowWidth,windowHeight))
running = True

# Game Title and Icon

title = "Spaceship Game"
pygame.display.set_caption(title)

# Plain Surface

Surface = pygame.Surface((100,200))
Surface.fill("orange")
x = 100

# Importing an Image
player_surface = pygame.image.load(join("images", "player.png"))

while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    # Draw the Game
    display_surface.fill("darkgray")
    x += 0.1
    display_surface.blit(player_surface, (x,150))
    pygame.display.update()


pygame.quit()