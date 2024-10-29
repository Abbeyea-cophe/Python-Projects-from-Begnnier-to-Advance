from playsound import playsound
import time

CLEAR = '\033[2]'
CLEAR_AND_RETURN = '\033[H'

def alarm(seconds):
    timeElapsed = 0
    
    print(CLEAR)
    while timeElapsed < seconds:
        time.sleep(1)
        timeElapsed += 1
        
        timeLeft = seconds - timeElapsed
        minutesLeft = timeLeft // 60
        secondsLeft = timeLeft % 60
        
        print(f'{CLEAR_AND_RETURN}{minutesLeft : 02d} : {secondsLeft : 02d}')


    playsound('alarm.mp3')
    
minutes = int(input('How many minutes to wait: '))
seconds = int(input('How many seconds to wait: '))
totalSeconds = minutes * 60 + seconds

alarm(totalSeconds)