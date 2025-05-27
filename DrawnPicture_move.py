import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Smiley Face")

# Colors
YELLOW = (255, 223, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Smiley face settings
radius = 40
x, y = WIDTH // 2, HEIGHT // 2
dx, dy = random.choice([-3, 3]), random.choice([-3, 3])  # Random initial speed
#The smiley face is a circle with a radius of 40 pixels.
#x, y = WIDTH // 2, HEIGHT // 2
#Places the face in the center of the screen.
#Speed (dx, dy):
#The smiley moves randomly left/right (dx) and
#up/down (dy) by 3 pixels per frame.


# Game loop
running = True
while running:
    pygame.time.delay(30)  # Control speed
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move smiley
    x += dx
    y += dy
    #Updates the position by adding dx
    #(horizontal movement) and dy (vertical movement).

    # Bounce off walls
    if x - radius <= 0 or x + radius >= WIDTH:
        dx = -dx
    if y - radius <= 0 or y + radius >= HEIGHT:
        dy = -dy
    #If the left or right edge is hit → Reverse dx (change direction).
    #If the top or bottom edge is hit → Reverse dy (change direction)

    # Drawing
    screen.fill(WHITE)  # Clear screen
    pygame.draw.circle(screen, YELLOW, (x, y), radius)  # Face
    pygame.draw.circle(screen, BLACK, (x - 15, y - 10), 5)  # Left eye
    pygame.draw.circle(screen, BLACK, (x + 15, y - 10), 5)  # Right eye
    pygame.draw.arc(screen, BLACK, (x - 20, y - 10, 40, 30), 3.14, 6.28, 3)  # Smile
    
    pygame.display.update()  # Refresh screen

pygame.quit()
