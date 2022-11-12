import pygame
import random
import os
import pygame.mixer

pygame.mixer.init()

pygame.init()

#Defining colours
white = (255,255,255)
red = (57, 204, 111)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)

#Creating gamewindow i.e. size of game window
scwid = 750  # width of window
schigh = 500 # height of window
gamewin = pygame.display.set_mode((scwid,schigh))

#Backgroung image
bgimage = pygame.image.load('ba1.jpg')
bgimage = pygame.transform.scale(bgimage ,(scwid,schigh)).convert_alpha()
print(bgimage)

#Homepage image
homeimage=pygame.image.load('homepage.jpg')
homeimage = pygame.transform.scale(homeimage ,(scwid,schigh)).convert_alpha()

#Gameover image
gameoverimage=pygame.image.load('gameoverwindow.jpg')
gameoverimage = pygame.transform.scale(gameoverimage ,(scwid,schigh)).convert_alpha()

#Creating title of the game
pygame.display.set_caption("Snakes")
pygame.display.update()

clock = pygame.time.Clock()  #Defining clock

#Creating font type
font = pygame.font.SysFont(None,50)

#Define function for displaying our score
def score_screen(text,color,x,y):
    score_text = font.render(text,True,color)
    gamewin.blit(score_text,[x,y])


#Defining function for shape,color,size of our snake
def plot_snk(gamewin, color, snk_list ,snake_radius):
    for x,y in snk_list:
        pygame.draw.circle(gamewin, color, [x,y], snake_radius)

def welcome():
    exit_game = False
    while not exit_game:
        gamewin.fill((150,150,150))
        #score_screen("Welcome to Snakes",black,200,75)
        #score_screen("Press Space Bar To Play", green, 160, 125)
        #Homepage image
        gamewin.blit(homeimage, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    pygame.mixer.music.load("bg_audio.mp3")    #Background music
                    pygame.mixer.music.play(100)                  #Starting Background music
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)


#Game loop
def gameloop():

    #Defining random colours
    a = random.randint(20, 250)
    b = random.randint(20, 250)
    c = random.randint(20, 250)

    # Game required variable
    exit_game = False
    game_over = False

    # Initial position of snake
    snake_x = 375
    snake_y = 250

    # Initial size of snake
    snake_size = 12   #For rectangular snake
    snake_radius = 8   #For circular snake

    # Default velocity of snake
    vel_x = 0
    vel_y = 0

    # Initial velocity of snake
    ini_vel = 3

    # Variables for increasing length of our snkake
    snk_list = []
    len_of_snk = 1  # initial length of snake

    # Number of times the screen is updated per second
    fps = 60  # Defining Frames Per Seconds for our game

    # Snake's Food
    food_x = random.randint(75, scwid / 2)
    food_y = random.randint(50, schigh / 2)

    # Setting DEFAULT value of score i.e. initial code
    score = 0
    
    #Checking existence of highscore.txt
    if (not os.path.exists("highscore.txt")):
                with open ("highscore.txt","w") as fo:
                    fo.write("0")
    
    # Reading highscore file
    with open("highscore.txt", "r") as fo:
        hi_score = fo.read()

    #Main Game Loop Begins

    while not exit_game:
        if game_over:
            #Modifying new high score
            with open("highscore.txt", "w") as fo:
                fo.write(str(hi_score))
            
            gamewin.fill(black)   # Not required if use background images
            #score_screen("Game Over!!  Press Enter To Continue",red,68,schigh/2)  #Displaying Game Over Message
            gamewin.blit(gameoverimage, (0, 0))
            score_screen("Score: " + str(score), (255, 142, 82), 290, 140) # Printing Score In Game Over Screen

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                #Defining actions on keypress
                #Defining controls of our snake
                if event.type == pygame.KEYDOWN:

                    # Defining controls
                    if event.key == pygame.K_RIGHT:   #Defining right control
                        vel_x= ini_vel
                        vel_y=0

                    if event.key == pygame.K_LEFT:    #Defining left control
                        vel_x=-ini_vel
                        vel_y=0

                    if event.key == pygame.K_UP:      #Defining up control
                        vel_x =0
                        vel_y =-ini_vel

                    if event.key == pygame.K_DOWN:    #Defining down control
                        vel_x =0
                        vel_y =ini_vel

                    # Assigning escape key to exit the game
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

                    #if event.key == pygame.K_w:
                    #    score +=10

            #Implimenting velocity to our snake
            snake_x = snake_x + vel_x
            snake_y = snake_y + vel_y

            #Creating score generator and condition for successful eating of food (i.e. Successful updation of store)
            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score += 10     #Updating Score

                #Updating position of our food
                food_x = random.randint(75, scwid / 2)
                food_y = random.randint(50, schigh / 2)

                #Changing color of food
                a = random.randint(20, 250)
                b = random.randint(20, 250)
                c = random.randint(20, 250)

                #Incresing length of our snake
                len_of_snk +=3

                #pygame.mixer.music.load("food.mp3")  # Game over sound effect

                #pygame.mixer.music.play()  # Starting gameover sound
                if score>int(hi_score):    #Defining High Score For The Game
                    hi_score = score


            # Colouring our game window
            gamewin.fill(white)   #Not neccesary if i use background image

            # Backgroung image
            gamewin.blit(bgimage, (0, 0))

            #Displaying Score + High Score In Game Window
            score_screen("Score: " + str(score) + " High Score: " + str(hi_score), blue, 10, 10)


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>len_of_snk:
                del snk_list[0]

            #Loop for self colliding
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")       #Game over sound effect
                pygame.mixer.music.play()                     #Starting gameover sound

            if snake_x<0 or snake_x>scwid or snake_y<0 or snake_y>schigh:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")       #Game over sound effect
                pygame.mixer.music.play()                     #Starting gameover sound

            #definig the SHAPE , DEFAULT position and SIZE of our snake
            #pygame.draw.circle(gamewin,red,[snake_x, snake_y],8)
            plot_snk(gamewin,red,snk_list ,snake_radius)

            # definig the SHAPE , DEFAULT position and SIZE of our snake's food
            pygame.draw.circle(gamewin, (a,b,c), [food_x, food_y],8)

        # update our display to execute every change in movement of snake and food
        pygame.display.update()

        # Providing fps to our game
        clock.tick(fps)


    pygame.quit()
    quit()

#Calling our function to impliment homescreen 
welcome()
