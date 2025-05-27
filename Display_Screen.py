import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window dimensions
width, height = 800, 600  # Width and height of the window
screen = pygame.display.set_mode((width, height))  # Create the window
pygame.display.set_caption("Basic Pygame Window")  # Set the window title

# Set a color for the background (R, G, B format)
background_color = (30, 144, 255)  # Example: Dodger Blue

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit event
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
