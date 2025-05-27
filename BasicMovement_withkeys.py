import pygame
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
#explain to them you can set the sixe of the screen 2 ways
#1. My creating variables and referring to the variables in the parameter
#2. directly putting the dimensions inside the parameters 

x = 50
y = 50
width = 40
height = 60
vel = 5
#x, y: The starting position of the rectangle (50 pixels from the top left).
#width, height: The size of the rectangle.
#vel: The speed at which the rectangle moves.

run = True
while run:
    pygame.time.delay(100)
    #Adds a small delay (100 milliseconds) between each frame to control the speed of the game.

    for event in pygame .event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    #pygame.key.get_pressed(): Checks which keys are currently being pressed.
    #K_LEFT, K_RIGHT, K_UP, K_DOWN: Move the rectangle left, right, up, or down by subtracting or adding vel (5 pixels).

    win.fill((0,0,0))
    pygame.draw.rect(win,(255, 0, 0), (x, y, width, height))
    pygame.display.update()
    #win.fill((0,0,0)): Clears the screen by filling it with black ((0,0,0)).
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)): Draws the red rectangle at the new (x, y) position.
    #pygame.display.update(): Updates the screen so changes appear.

pygame.quit()
