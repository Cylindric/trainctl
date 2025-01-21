print(f"In LED module __package__:{__package__}, __name__:{__name__}")

class LED:
    def __init__(self, x, y, state=False):
        self.on = state
        self.x = x
        self.y = y
    
    def draw(self):
        if self.on:
            return "▓"
        else:
            return "░"
