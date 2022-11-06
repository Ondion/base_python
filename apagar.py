from enum import Enum
from random import randint

class Frame:
    PINS = 10
    

    def __init__(self):
        self.first_roll = 0
        self.second_roll = 0
        self.type = FrameTypes.UNPLAYED


    def play(self):
        self.first_roll = self._roll()
        pins_left = self.PINS - self.first_roll
        self.second_roll = self.roll(pins_left)
        self.type = FrameTypes.REGULAR

    @classmethod  
    def _roll(cls, pins_left = PINS):
        return randint(0, pins_left)
      
    def change():
        return []
      
        
class FrameTypes(Enum):
    UNPLAYED = 0
    REGULAR = 1
    SPARE = 2
    STRIKE = 3

