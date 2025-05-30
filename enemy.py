import pygame
import  os
pygame.init()

# Set the correct path to the image directory
img_dir = r"C:\Users\tahre\Downloads\pygame\Animation_and_sprites\Animation_Images\Game"

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

# Load images with full path
#The hero has 9 images for walking right and 9 for walking left.The hero has 9 images for walking right and 9 for walking left.
walkRight = [pygame.image.load(os.path.join(img_dir, f'R{i}.png')) for i in range(1, 10)]
walkLeft = [pygame.image.load(os.path.join(img_dir, f'L{i}.png')) for i in range(1, 10)]
bg = pygame.image.load(os.path.join(img_dir, 'bg.jpg'))
char = pygame.image.load(os.path.join(img_dir, 'standing.png'))

clock = pygame.time.Clock()


#This class stores all the hero's information, like position, size, speed, and movement.
#The draw() function chooses the right image depending on if the hero is moving left or right.
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        
    # Draws the correct walking animation based on movement direction.
    # If the player is standing still, it displays the first frame of walking animation.
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
                

#Represents bullets shot by the player.
#Moves left (-1) or right (1) depending on player direction.
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    img_dir = r"C:\Users\tahre\Downloads\pygame\Animation_and_sprites\Animation_Images\Game"

    walkRight = [pygame.image.load(os.path.join(img_dir, f'R{i}E.png')) for i in range(1, 10)]
    walkLeft = [pygame.image.load(os.path.join(img_dir, f'L{i}E.png')) for i in range(1, 10)]

    # x, y, width, height: Defines enemy position and size.
    # path: Defines start and end points of movement.
    # walkCount: Controls animation.
    # vel: Controls enemy movement speed.
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        
    # Displays the correct walking animation.
    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            
    # Moves back and forth between the start (x) and end (end) positions.    
    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        

# Clears the screen and redraws the background, player, enemy, and bullets.
def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()
    


# mainloop
# Creates a player (man), enemy (goblin), and a list of bullets.
# Runs 27 times per second to control the game speed.
# 
man = player(200, 410, 64,64)
goblin = enemy(100, 410, 64, 64, 300)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    # Moves bullets across the screen.
    # Removes bullets if they go off-screen.
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    # Checks which keys are pressed.
    keys = pygame.key.get_pressed()
    
    # Shoots bullets in the direction the player is facing.
    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()
