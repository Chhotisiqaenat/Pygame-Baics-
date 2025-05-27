import pygame
import os  # Import the os module

pygame.init()

# Set the correct path to the image directory
img_dir = r"C:\Users\tahre\Downloads\pygame\Animation_and_sprites\Animation_Images\Game"

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

# Load images with full path
walkRight = [pygame.image.load(os.path.join(img_dir, f'R{i}.png')) for i in range(1, 10)]
walkLeft = [pygame.image.load(os.path.join(img_dir, f'L{i}.png')) for i in range(1, 10)]
bg = pygame.image.load(os.path.join(img_dir, 'bg.jpg'))
char = pygame.image.load(os.path.join(img_dir, 'standing.png'))
#The game uses multiple images to create an animation effect.
#walkRight & walkLeft lists contain 9 images each to show the walking motion.
#bg is the background image.
#char is the standing character image.

x = 50
y = 400
width = 40
height = 60
vel = 5
#The character starts at position (50, 400).
#The vel variable controls how fast the character moves (5 pixels per frame).

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0
#clock = pygame.time.Clock() controls the game speed (frame rate).
#isJump keeps track of whether the player is jumping.
#jumpCount controls the jump height.
#left and right track which direction the character is moving.
#walkCount keeps track of which walking image to display.

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
#This function updates the screen in every frame.
#Walking Animation:
#The character cycles through walkLeft or walkRight images every 3 frames (walkCount//3).
#If the character isn't moving, the standing image is displayed.
#pygame.display.update() refreshes the screen with the new character position.


run = True

while run:
    clock.tick(27)
    #The while loop keeps the game running until the player quits.
    #clock.tick(27) sets the game speed so everything runs smoothly.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
        #If the left arrow key is pressed, the character moves left.
        #x -= vel decreases x-position, moving left.
        #left = True activates left animation.

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        #If the right arrow key is pressed, the character moves right.
        #x += vel increases x-position, moving right.
        #right = True activates right animation.
        
    else: 
        left = False
        right = False
        walkCount = 0
        #If no keys are pressed, the character stops moving, and the animation resets.

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
            #When not already jumping, pressing SPACE makes the character jump.
            #It stops walking animations during the jump.


    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
            #Jumping follows a parabolic curve using (jumpCount * abs(jumpCount)) * 0.5.
            #The character moves up first (y decreases), then comes back down.

    redrawGameWindow() 
    
    
pygame.quit()
