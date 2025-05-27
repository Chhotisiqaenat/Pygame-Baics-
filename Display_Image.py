import pygame
#Pygame is a library used for making games and graphics in Python.
#We need to import it first before we can use any of its features.

# Initialize Pygame
pygame.init()
#This starts Pygame and gets everything ready for our program.

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Display Image at Center")
#We create a window that is 600 pixels wide and 400 pixels tall.
#pygame.display.set_mode() sets up the screen where our game will run.
#pygame.display.set_caption() gives the window a title.

# Load the image
image = pygame.image.load('rose.png')
#This loads an image file named rose.png into the program.
#The image must be in the same folder as your Python script, or you need to provide the correct path.

# Get the dimensions of the image
image_width, image_height = image.get_size()
#This finds out how big the image is (its width and height in pixels).

# Calculate the center position
center_x = (screen_width - image_width) // 2
center_y = (screen_height - image_height) // 2
#These formulas ensure the image appears exactly in the middle of the screen.
#We subtract the image size from the screen size and divide by 2.

# Define colors
white = (255, 255, 255)

# Run the game loop
#This keeps the game running until we decide to close it.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Pygame listens for events like key presses or clicking the close button.
    #If the user clicks the X button on the window, the game stops.

    # Fill the background with white
    screen.fill(white)

    # Display the image at the calculated center position
    screen.blit(image, (center_x, center_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
