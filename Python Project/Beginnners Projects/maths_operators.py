import random
import time

OPERATOR = ['+',  '-' , '*']
MIN_OPERAND = 2
MAX_OPERAND = 20
TOTAL_PROBLEMS = 10

def generateProblem():
    left = random.randint(MIN_OPERAND , MAX_OPERAND)
    right = random.randint(MIN_OPERAND , MAX_OPERAND)
    operator = random.choice(OPERATOR)
    
    expr = str(left) + ' ' +  operator + ' ' + str(right)
    answer = eval(expr)
    return expr , answer

wrong = 0
input('Please press enter to start!')
print('------------------------')

startTime = time.time()

for i in range(TOTAL_PROBLEMS):
    expr , answer = generateProblem()
    while True:
        guess = input('Problem #' + str(i + 1) + ':' + expr + '=')
        if guess == str(answer):
            break
        wrong += 1
        
endTime = time.time()
totalTime = round(endTime - startTime, 2)

print('-----------------------')
print('Nice work! You finished', totalTime,'seconds!')