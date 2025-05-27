import pygame

# Initialize Pygame
pygame.init()

# Load the image
background_image = pygame.image.load("background.jpg")  # Replace with your image path

# Set screen size to match image size
screen = pygame.display.set_mode(background_image.get_size())

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Draw the background image
    screen.blit(background_image, (0, 0))

    #Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
