import pygame

pygame.init()
windowWidth, windowHeight = 1280, 720
display_surface = pygame.display.set_mode((windowWidth,windowHeight))
running = True

# Game Title and Icon

title = "Spaceship Game"
pygame.display.set_caption(title)

while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("darkorchid")


    # Draw the Game
    pygame.display.update()


pygame.quit()