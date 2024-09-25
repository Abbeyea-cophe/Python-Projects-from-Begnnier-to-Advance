print('Welcome to the Game')

playing = input('Do you want to play?  ')
score = 0
if playing.lower() != 'yes':
    quit()
print("Okay Let's play")

answer = input( "What dose CPU stands for ? ")
if answer.lower() == 'central processing unit':
    print ("That's correct")
    score += 10
else:
    print("That's  incorrect. The computer's brain is called a Central Processing Unit (CPU)")
    
answer = input( "What dose GPU stands for ? ")
if answer.lower() == 'graphic processing unit':
    print ("That's correct")
    score += 10
else:
    print("That's  incorrect. The correct answer is Graphic Processing Unit (GPU)")
    
answer = input( "What dose ROM stands for ? ")
if answer.lower() == 'read only memory':
    print ("That's correct")
    score += 10
else:
    print("That's  incorrect. The correct answer is Read Only Memory (ROM)")

print('You got',score,'out of 3 questions right!')
print('That means, you got',(score/3)*100,'%')