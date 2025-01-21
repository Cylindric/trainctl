import curses
import time
# # from . import LED

from colour import Colour
from layout import Layout
from led import LED


print(f"In CTL module __package__:{__package__}, __name__:{__name__}")

# Each layout has zero or more turnouts
# Each turnout has two blocks after it
# Each block contains zero or more LEDs
# Each LED can be on or off


def main(stdscr):
    curses.start_color()
    stdscr.clear()
    stdscr.nodelay(True)
    curses.curs_set(0)  # Hide the cursor

    curses.init_pair(Colour.BLOCK1.value, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(Colour.BLOCK2.value, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(Colour.BLOCK3.value, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(Colour.BLOCK4.value, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(Colour.POINT_ON.value, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(Colour.POINT_OFF.value, curses.COLOR_RED, curses.COLOR_BLACK)    
    

    layout = Layout()

    keep_looping = True
    last_frame_ms = 0
    while(keep_looping):
        # get current milliseconds
        time_ms = int(round(time.time() * 1000))

        # if 1000ms have passed since last frame
        if time_ms - last_frame_ms >= 10:
            # update the frame
            last_frame_ms = time_ms
            layout.load_from_file('data.yaml')
            stdscr.clear()
            layout.draw(stdscr)
            stdscr.refresh()

        c = stdscr.getch()
        if c == 27: # ESC key
            keep_looping = False
        
        for i in range(0, 8):
            if c == ord(str(i+1)):
                if layout.turnouts.get(i+1) is not None:
                    layout.turnouts.get(i+1).toggle()

if __name__ == "__main__":
    curses.wrapper(main)