import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Shapes")
#Purpose: Sets the window size to 400x400 pixels, creating a square window.
#Explain that the screen's size can affect how the shapes are displayed.


# Define colors
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(white)

    # Draw shapes
    pygame.draw.rect(screen, red, (100, 100, 50, 50))  # Red square
    #screen: Where to draw the rectangle (the game window).
    #red: The color of the rectangle.
    #(100, 100, 50, 50):
    #(100, 100): The top-left corner of the rectangle.
    #50, 50: The width and height of the rectangle.
    #Explanation: This creates a red square with size 50x50 at position (100, 100).

    pygame.draw.circle(screen, green, (200, 200), 40)  # Green circle
    #screen: Where to draw the circle.
    #green: The color of the circle.
    #(200, 200): The center of the circle.
    #40: The radius of the circle.
    #Explanation: This creates a green circle with a radius of 40 pixels, centered at position (200, 200).

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
