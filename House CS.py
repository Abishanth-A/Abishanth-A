import pygame

import math

pygame.init()

 

# Define some colors

BLACK    = (   0,   0,   0)

WHITE    = ( 255, 255, 255)

GREEN    = (   0, 255,   0)

RED      = ( 153,   0,   0)

blue    =   0,   205, 255

YELLOW = (255, 255, 0)

blue =list(blue)

BROWN = (102, 51, 0)

LIGHT_BROWN = (153, 76, 0)

 

# Loop until the user clicks the close button.

done = False

 

# Used to manage how fast the screen updates

clock = pygame.time.Clock()

 

size = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Abishanth' House Simulator")

# Loop until the user clicks the close button.

done = False

 

# Used to manage how fast the screen updates

clock = pygame.time.Clock()

#Global Variables

 

x_val = 15

y_val = 100

offset = 1

# -------- Main Program Loop -----------

while not done:

    # --- Main event loop

    for event in pygame.event.get(): # User did something

        if event.type == pygame.QUIT: # If user clicked close

            done = True # Flag that we are done so we exit this loop

 

    # --- Game logic should go here

    x_val += 3

    y_val = 24/6125 * x_val ** 2 + -2.738938776 * x_val + 500

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands

    # above this, or they will be erased with this command.

    screen.fill(blue)

    if (blue[1] > 0):

        blue[1] -= 1

        blue[2] -= 1

    #Draw here

    pygame.draw.circle(screen, YELLOW, [x_val, y_val], 20)

    pygame.draw.rect(screen, BROWN, [250,300,200,300])

    pygame.draw.rect(screen, BLACK, [375,175,50,100])

    pygame.draw.rect(screen, WHITE, [375,350,50,50])

    pygame.draw.rect(screen, WHITE, [275,350,50,50])

    pygame.draw.rect(screen, LIGHT_BROWN, [325,425,50,75])

    pygame.draw.circle(screen, YELLOW, [360, 475 ], 5)

    pygame.draw.polygon(screen,RED,[(200,300), (500,300), (350,200)])

    # --- Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

   

    # --- Limit to 60 frames per second

    clock.tick(60)

 #end while

 

pygame.quit()