import curses
import yaml

from block import Block
from turnout import Turnout

print(f"In Layout module __package__:{__package__}, __name__:{__name__}")

class Layout:
    turnout_list_coords = {'x': 0, 'y': 0}

    def __init__(self):
        self.reset()

        # self.turnouts = []
        # self.turnouts.append(Turnout(13, 15))
        # self.turnouts.append(Turnout(9, 13))
        # self.turnouts.append(Turnout(13, 13))
        # # self.turnouts.append(Turnout(13, 13))
        # # self.turnouts.append(Turnout(13. 13))
        # self.turnouts.append(Turnout(8, 4))
        # self.turnouts.append(Turnout(12, 6))


    def reset(self):
        self.blocks = {}
        self.turnouts = {}

    def load_from_file(self, filename):
        self.reset()

        with open(filename, 'r', encoding='utf8') as file:
            data = yaml.safe_load(file)
            for block in data['blocks']:
                b = Block().from_yaml(block)
                self.blocks[block['name']] = b
            
            for turnout in data['turnouts']:
                t = Turnout().from_yaml(turnout)
                self.turnouts[turnout['name']] = t
        

    def draw(self, stdscr):
        for block in self.blocks.values():
            block.draw(stdscr)
        
        for turnout in self.turnouts.values():
            turnout.draw(stdscr)
        
        # Turnout icon list
        col = self.turnout_list_coords['x']
        for t in self.turnouts.values():
            if t.state:
                stdscr.addstr(self.turnout_list_coords['y'], col, t.get_symbol(), curses.color_pair(t.get_colour()))
            else:
                stdscr.addstr(self.turnout_list_coords['y'], col, t.get_symbol(), curses.color_pair(t.get_colour()))
            col+=1
