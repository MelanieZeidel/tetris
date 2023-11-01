import pygame, sys

#initialize the game
pygame.init()

#display surface of the game window setting height and width
#set_mode(width,height) method takes a tuple as an argument
#the board height and widht starts on the left top of the graphic
#(0,10) moves down and (10,0) moves to the right
screen = pygame.display.set_mode((300,600))

#create a title
pygame.display.set_caption('Tetris Game')

# set the timer for calculate the time and modfy
# the speed of the game
clock = pygame.time.Clock()

#gameloop: event handling, update positions and drawing objects
while True:
    #event handling
    for event in pygame.event.get():
        #quick event closing the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    #tick() method takes an integer as an argument and is the number of frames per second
    clock.tick(60)
    