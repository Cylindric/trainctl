import curses

from colour import Colour

print(f"In Turnout module __package__:{__package__}, __name__:{__name__}")

class Turnout:
    def __init__(self, x=0, y=0):
        self.reset()
        self.position = {'x': x, 'y': y}
    
    def reset(self):
        self.state = True
        self.position = {'x': 0, 'y': 0}

    def from_yaml(self, yaml):
        self.reset()
        self.position = yaml['position']
        return self

    def draw(self, stdscr):
        stdscr.addstr(self.position['y'], self.position['x'], self.get_symbol(), curses.color_pair(self.get_colour()))
    
    def get_symbol(self):
        return '█'

    def get_colour(self):
        if self.state:
            return Colour.POINT_ON.value
        else:
            return Colour.POINT_OFF.value
    
    def toggle(self):
        self.state = not self.state
