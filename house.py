import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 500
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("House Drawing")

# Define colors
brown = (139, 69, 19)
red = (255, 0, 0)
blue_sky = (135, 206, 235)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with blue (sky color)
    screen.fill(blue_sky)

    # Draw the house base
    pygame.draw.rect(screen, brown, (150, 150, 200, 150))  # Brown rectangle

    # Draw the roof
    pygame.draw.polygon(screen, red, [(150, 150), (250, 50), (350, 150)])  # Red triangle

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
