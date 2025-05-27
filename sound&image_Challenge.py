import pygame
import random  # To change background color randomly

# Initialize Pygame
pygame.init()
pygame.mixer.init()  # Initialize sound mixer

# Set up display
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Image & Sound Player")

# Load assets
image = pygame.image.load('rose.png')  # Replace with your image file
sound = pygame.mixer.Sound('piano.mp3')  # Replace with your sound file

# Get image dimensions
image_width, image_height = image.get_size()
center_x = (screen_width - image_width) // 2
center_y = (screen_height - image_height) // 2

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
background_color = white  # Default background color

# Set up font
font = pygame.font.SysFont(None, 36)

# Function to display text
def display_text(message, x, y):
    text = font.render(message, True, black)
    screen.blit(text, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play sound when 'P' is pressed
                sound.play()
            elif event.key == pygame.K_c:  # Change background color when 'C' is pressed
                background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color

    # Fill background
    screen.fill(background_color)

    # Display image
    screen.blit(image, (center_x, center_y))

    # Display instructions
    display_text("Press 'P' to play sound", 180, 320)
    display_text("Press 'C' to change background", 140, 350)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
