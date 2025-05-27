import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Image in Pygame")

WHITE = (255, 255, 255)

# Load the image
image = pygame.image.load('rose.png')
image_width, image_height = image.get_size()

# Initial position and speed
image_x, image_y = 50, 50
image_speed_x, image_speed_y = 5, 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Move the image
    image_x += image_speed_x
    image_y += image_speed_y
    
    # Bounce off the edges
    if image_x <= 0 or image_x + image_width >= WIDTH:
        image_speed_x = -image_speed_x
    if image_y <= 0 or image_y + image_height >= HEIGHT:
        image_speed_y = -image_speed_y

    # Draw everything
    screen.fill(WHITE)
    screen.blit(image, (image_x, image_y))  # Draw image instead of rectangle
    pygame.display.flip()
    
    clock.tick(60)  # Limit to 60 FPS
