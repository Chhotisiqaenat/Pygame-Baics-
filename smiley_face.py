import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 500
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smiley Face Drawing")

# Define colors
yellow = (255, 255, 0)
black = (0, 0, 0)
blue_sky = (135, 206, 235)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with blue (sky color)
    screen.fill(blue_sky)

    # Draw the face
    pygame.draw.circle(screen, yellow, (250, 200), 100)  # Yellow face

    # Draw the eyes
    pygame.draw.circle(screen, black, (220, 180), 10)  # Left eye
    pygame.draw.circle(screen, black, (280, 180), 10)  # Right eye

    # Draw the smiling mouth
    pygame.draw.arc(screen, black, (200, 190, 100, 50), math.pi, 2 * math.pi, 5)
    # Smiling mouth
    #pygame.draw.arc() → Draws an arc on the screen.
    #screen → The surface where the arc is drawn.
    #black → The color of the arc (assuming black is defined as (0, 0, 0) earlier in the code).
    #(200, 190, 100, 50) → Defines a rectangle (x, y, width, height), which is the bounding box for the arc:
    #200, 190 → Top-left corner of the bounding box.
    #100, 50 → Width and height of the bounding box.
    #math.pi, 2 * math.pi → Defines the arc's start and end angles:
    #math.pi (π) → Starts at 180° (left side).
    #2 * math.pi (2π) → Ends at 360° (right side).
    #This creates a downward-facing arc, resembling a smile. 😊
    #5 → The thickness of the arc in pixels.


    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
