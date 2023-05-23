import pygame
import random

# initialize the game
pygame.init()

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

# window size
size = (700,500)
screen = pygame.display.set_mode(size)
# window title
pygame.display.set_caption("Alex's Game") 

# empty list for loop
random_list = []

# loop for random position 
for i in range(50):
    x = random.randrange(0,400)
    y = random.randrange(0,400)
    random_list.append([x,y])

# --------Interacting with the user---------

# lopp until the user clicks the close button
done = False

# to manage how fast the screen updates
clock = pygame.time.Clock()

#starting position of the rectangle
rect_x = 50
rect_y = 50

# speed and direction
rect_change_x = 5
rect_change_y = 5

# ---------- Main Program Loop --------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if the user clicks close
            done = True
    for i in range(50):
        x = random.randrange(0, 400)
        y = random.randrange(0, 400)
        pygame.draw.circle(screen, WHITE, [x, y], 2)

# ---------- Drawing Code --------------

    # screen background
    screen.fill(BLACK)

    #draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x,rect_y,50,50])

    # to move the rectangle from the starting point
    rect_x += rect_change_x 
    rect_y += rect_change_y

    # to bounce the rectangle
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

# to update the screen when we draw
    pygame.display.flip()

# quit the program
pygame.quit()