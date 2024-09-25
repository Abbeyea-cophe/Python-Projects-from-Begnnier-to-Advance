import turtle
import time
import random

# CONSTANT VARIABLES
WIDTH , HEIGHT = 500 , 500
COLORS = ['red', 'blue' , 'pink', 'cyan', 'black', 'orange', 'violet', 'indigo', 'yellow', 'brown']


# CREATING THE NUMBER OF RACERS IN THE GAME
def numberOfRacers():
    racers = 0
    while True:
        racers = input('Please enter the number of racers (2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Invalid input. Please enter a number.')
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print('Oops sorry, the number is not in range of 2 - 10')


# CREATING THE GAME FOR THE USERS WITH THE  INPUT OF RACERS
def createGame(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i , color in enumerate(colors):
        
        game = turtle.Turtle()
        game.color(color)
        game.shape('turtle')
        game.left(90)
        game.penup()
        game.setpos(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20 )
        game.pendown()
        turtles.append(game)
        
    return turtles


# CREATING THE RACING GAME
def createRace(colors):
    turtles = createGame(colors)
    
    while True:
        for game in turtles:
            distance = random.randrange(1 , 20)
            game.forward(distance)
            
            x , y = game.pos()
            if  y >= HEIGHT // 2 - 10:
                return colors[turtles.index(game)]
            
            
            
# CREATING THE TURTLE  SCREEN
def initTurtle():
    screen = turtle.Screen()
    screen.setup(WIDTH , HEIGHT)
    screen.title('Turtle Racing')


# CALLING OF FUNCTIONS
racers = numberOfRacers()
initTurtle()


random.shuffle(COLORS)
colors = COLORS[:racers]

winner = createRace(colors)
print('The winner of the race is', winner ,'turtle')
time.sleep(3)