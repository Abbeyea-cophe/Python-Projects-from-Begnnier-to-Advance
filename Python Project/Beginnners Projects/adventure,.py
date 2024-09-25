name = input('What is your name?: ')
print('Welcome', name, 'to this adventure!')

playing = input('Do you want to play!: ')
if playing.lower() != 'yes':
    quit()
print ('Okay lets play')

answer = input('You are in a jungle running for your life and you have come to a junction. You can turn left or right , now make your choice.: ').lower()
if answer == 'left':
    answer = input('You come to a river , you can walk around it or swim accross?Type walk to around & swim to swim accross: ' )
    
    if answer == 'swim':
        print("You swam acroos and you were eaten by an alligator")
    elif answer == 'walk':
        print("You waked for many miles , and run out of water and die")
    else:
        print('Not a vlid choice')
    
elif answer == 'right':
    answer = input('You have come to a Bridge , it looks wobbly, do you cross or go back. (cross / back):  ')

    if answer == 'back':
        print("You went back! You have lost")
    elif answer == 'cross':
        answer = input ('You cross the Bridge and you met a stranger, do talk to him. (yes / no ):  ')
        
        if answer == 'no':
            print('You ignored the stranger and ypu were killed by him')
            
        elif answer == 'yes':
            print('You talked to the stranger and he gave you direction and gold. Congratulation you won the game!!!')
        else:
            print('Not a valid choice')
    else:
        print('Not a valid choice')
else:
    print('Not a valid choice')

print ('Thank you for playing', name)