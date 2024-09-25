import random

def roll():
    minValue = 1
    maxValue = 2
    roll = random.randint(minValue, maxValue)
    
    return roll

while True:
    players = input('Enter the numbers of players (2 - 4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Must be between 2 - 4 players.')
    else:
        print('Invalid, try again')
print(players, 'players are playing this game')


maxScore = 50
playerScore = [0 for _ in range(players)]


while max(playerScore) < maxScore:
    
    for playerIdx in range(players):
        print('\n Player number', playerIdx + 1 , 'turn has just started!\n')
        print ('Your total score is: ', playerScore[playerIdx], '\n')
        currentScore = 0
    
        while True:
                shouldRoll = input('would you like to roll (y)? ')
                if shouldRoll.lower() != 'y':
                    break
    
                value = roll()
                if value == 1:
                    print('You rolled a 1! Turn done!')
                    currentScore = 0
                    break
                else:
                    currentScore += value
                    print('You rolled a :', value)
                    
                print('Your score is', currentScore)
    
    playerScore[playerIdx] += currentScore
    print('Your total score is: ', playerScore[playerIdx])
    

maxScore = max(playerScore)
winningIdx = playerScore.index(maxScore)
print('Player number', winningIdx + 1 , 'is the winner of the game with the of:',maxScore)