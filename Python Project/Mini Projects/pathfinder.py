import curses
from  curses import wrapper
import time
import queue



maze = [
    ['#','#','#','#','#', 'O','#','#','#'],
    ['#',' ',' ',' ',' ', ' ',' ',' ','#'],
    ['#',' ','#','#',' ', '#','#',' ','#'],
    ['#',' ','#',' ',' ', ' ','#',' ','#'],
    ['#',' ','#',' ','#', ' ','#',' ','#'],
    ['#',' ','#',' ','#', ' ','#',' ','#'],
    ['#',' ','#',' ','#', ' ','#','#','#'],
    ['#',' ',' ',' ',' ', ' ',' ',' ','#'],
    ['#','#','#','#','#', '#','#','X','#']
]





 
def  main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_PAIRS)
    
    
    # stdscr.clear()
    # stdscr.addstr(5, 5, 'Hello world!')
    # stdscr.refresh()
    # stdscr.getch()

wrapper (main)