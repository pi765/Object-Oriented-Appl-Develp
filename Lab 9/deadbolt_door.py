# Lab 9
# Kamal Ali & William Nguyen
# 10/20/2024
# A deadbolt door with 2 bolts that are randomly locked or unlocked

import random
from door import Door

class DeadboltDoor(Door):  # inherit from Door class
    def __init__(self):
        self.unlocked = False  # door is locked
        self.bolt = []
        boltlock1 = random.randint(1,2) # 50% chance to be locked or unlocked
        boltlock2 = random.randint(1,2)
        self.state = 0          # partial or complete lock of the door
        if boltlock1 == 1:      # bolt 1 is locked
            self.bolt.append(1)
        if boltlock2 == 1:      # bolt 2 is locked
            self.bolt.append(2)
        if len(self.bolt) == 0: # no bolts were locked
            self.unlocked = True
        elif len(self.bolt) == 1:
            self.state = 1      # partial unlock

    def examine_door(self):
        return f"You encounter a double deadbolt door, both deadbolts must be unlocked to open it, but you can't tell from looking at them whether they're locked or unlocked."
   
    def menu_options(self):
        return f"1. Toggle Bolt 1\n2. Toggle Bolt 2"
   
    def get_menu_max(self):
        return 2            # number of bolts choices
   
    def attempt(self,option):
        if option == 1:
            if 1 in self.bolt:              # if bolt 1 isn't unlocked
                self.bolt.remove(1)         # unlock bolt 1
                if not self.bolt:           # if bolt list is empty
                    self.unlocked = True
                return f"You toggle the first bolt."
            else:
                self.state = len(self.bolt)             # bolt already unlocked, update state
                return f"You toggle the first bolt."
        else:
            if 2 in self.bolt:              # if bolt 1 isn't unlocked
                self.bolt.remove(2)         # unlock bolt 1
                if not self.bolt:           # if bolt list is empty
                    self.unlocked = True
                return f"You toggle the second bolt."
            else:
                self.state = len(self.bolt)             # bolt already unlocked, update state
                return f"You toggle the second bolt."

    def is_unlocked(self):
        return self.unlocked    # True if True, False if False
       
    def clue(self):
       if self.state == 1:  # 1 bolt locked
            return f"You jiggle the door... it seems like one of the bolts is unlocked"
       else:
           return f"You jiggle the door... it's completely locked." # both are locked
    
    def success(self):
        return f"You unlocked both deadbolts and opened the door."