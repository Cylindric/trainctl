from enum import Enum

print(f"In Colour module __package__:{__package__}, __name__:{__name__}")

class Colour(Enum):
    BLOCK1 = 1
    BLOCK2 = 2
    BLOCK3 = 3
    BLOCK4 = 4
    POINT_ON = 5
    POINT_OFF = 6
