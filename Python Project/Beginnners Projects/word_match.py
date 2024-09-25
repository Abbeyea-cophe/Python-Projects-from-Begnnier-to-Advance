import curses
import random
import time
from curses import wrapper


def startScreen(stdscr):
    
    stdscr.clear()
    stdscr.addstr('Welcome to the Tying Test Speed')
    stdscr.addstr('\nPlease press Enter to start the game')
    stdscr.refresh()
    stdscr.getkey()
    

def displayText(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f'WPM : {wpm}')
    for i , char in enumerate(current):
        correctChar = target[i]
        color = curses.color_pair(1)
        
        if char != correctChar:
            color = curses.color_pair(2)
            
        stdscr.addstr(0, i, char, color)



def loadText():
    with open('game.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()



def wpmTest(stdscr):
    targetText = loadText()
    currentText = []
    wpm = 0
    startTime = time.time()
    stdscr.nodelay(True)
    
    while True:
        
        timeElapsed = max(time.time() - startTime, 1)
        wpm = round((len(currentText) / (timeElapsed / 60)) / 5)
    
        stdscr.clear()
        displayText(stdscr, targetText, currentText, wpm)
        stdscr.refresh()
        
        if ''.join(currentText) == targetText:
            stdscr.nodelay(False)
            break
        
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        
        if key in ('KEY_BACKSPACE', '\b' ,'\x7f'):
            if len(currentText) > 0 :
                currentText.pop()
        elif len(currentText) < len(targetText):
            currentText.append(key)



def main(stdscr):
    
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_PAIRS)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    startScreen(stdscr)
    
    while True:
        wpmTest(stdscr)
        stdscr.addstr(2, 0, 'You have complete the game!, Please press any key to continue')
        key = stdscr.getkey()
        
        if ord(key)  == 27 :
            break
    
    
wrapper(main)