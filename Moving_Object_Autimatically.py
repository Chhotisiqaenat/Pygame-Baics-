import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Project")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

image = pygame.image.load('rose.png')
image_width, image_height = image.get_size()
rect_x, rect_y = 50, 50
#rect_width, rect_height = 60, 40
rect_speed_x, rect_speed_y = 5, 5
#The rectangle starts at (50, 50).
#It has a width of 60 pixels and a height of 40 pixels.
#rect_speed_x, rect_speed_y = 5, 5 means the rectangle moves 5 pixels per frame in both directions.

clock = pygame.time.Clock()
#Games run in a loop to keep updating the screen continuously.
#pygame.time.Clock() helps control the speed of the game.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    rect_x += rect_speed_x # Move the rectangle in the X direction
    rect_y += rect_speed_y # Move the rectangle in the Y direction
    
    if rect_x <= 0 or rect_x + rect_width >= WIDTH:
        rect_speed_x = -rect_speed_x
    if rect_y <= 0 or rect_y + rect_height >= HEIGHT:
        rect_speed_y = -rect_speed_y
        
    #if rect_x <= 0: If the rectangle touches the left wall, reverse its direction.
    #if rect_x + rect_width >= WIDTH: If the rectangle touches the right wall, reverse direction.
    #if rect_y <= 0: If it touches the top, reverse direction.
    #if rect_y + rect_height >= HEIGHT: If it touches the bottom, reverse direction.

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    
    clock.tick(60)
    #clock.tick(60) sets the game to 60 FPS, making it smooth.
