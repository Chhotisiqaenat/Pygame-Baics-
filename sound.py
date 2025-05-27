import pygame

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
pygame.mixer.init()
sound = pygame.mixer.Sound('piano.mp3')
#pygame.mixer is a part of Pygame that handles sounds and music.
#We initialize it so we can play sound effects.

# Load the sound
#This loads a sound file named piano.mp3.
#The file must be in the same folder as the script or the correct path must be provided.

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Play Sound Example")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up fonts
font = pygame.font.SysFont(None, 36)
#This creates a font for displaying text on the screen.
#None means we use the default system font.
#36 is the font size.

# Function to display text
def display_text(message, x, y):
    text = font.render(message, True, black)
    screen.blit(text, (x, y))
#This function renders text in black and places it at (x, y) on the screen.
#blit() is used to draw the text.

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play sound when the spacebar is pressed
                sound.play()
        #Event handling checks for user actions.
        #If the close button is clicked, the program stops.
        #If the spacebar (K_SPACE) is pressed, the sound plays.

    # Fill the background with white
    screen.fill(white)

    # Display instructions
    display_text("Press SPACE to play the sound", 150, 180)
    #display_text() shows instructions at the center of the screen.

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
