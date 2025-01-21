import curses

print(f"In Block module __package__:{__package__}, __name__:{__name__}")

from led import LED

class Block:
    def __init__(self, leds=[], x=0, y=0, colour=1):
        self.reset()
        self.leds = leds
        self.colour = colour
        self.position = {'x': x, 'y': y}

    def reset(self):
        self.leds = []
        self.colour = 1
        self.position = {'x': 0, 'y': 0}

    def from_yaml(self, yaml):
        self.reset()
        self.colour = yaml['colour']
        self.position = yaml['position']
        self.leds = [LED(led['x'], led['y']) for led in yaml['leds']]
        return self

    def draw(self, stdscr):
        for led in self.leds:
            stdscr.addstr(self.position['y'] + led.y, self.position['x'] + led.x, led.draw(), curses.color_pair(self.colour))