import pygame
import random
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
 
# Set the height and width of the screen
SIZE = [1000, 1000]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
 
# empty array for the snow animation
snow_list = []
 
# This will loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 1000)
    y = random.randrange(0, 1000)
    snow_list.append([x, y])
 
clock = pygame.time.Clock()
 
# Now we want the loop to work until the user clicks the close button

# so we define a variable with False
done = False

# while the user doesn't click the close button
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Process each snow flake in the list
    for i in range(len(snow_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
 
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
 
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 1000:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 1000)
            snow_list[i][0] = x
 
    # Update the screen
    pygame.display.flip()
    clock.tick(20)

# end the program 
pygame.quit()