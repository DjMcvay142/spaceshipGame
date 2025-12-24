import pygame

pygame.init()
windowWidth, windowHeight = 1280, 720
display_surface = pygame.display.set_mode((windowWidth,windowHeight))
running = True

while running:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("purple")

    # Draw the Game
    pygame.display.update()


pygame.quit()