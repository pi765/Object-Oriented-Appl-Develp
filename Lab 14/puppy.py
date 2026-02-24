# Lab 14
# Kamal Ali & William Nguyen
# 12/03/2025
# the puppy object that the user interacts with

from state_asleep import StateAsleep
class Puppy:
    def __init__(self):     # initialize
        self._state = StateAsleep()     # asleep
        self._feeds = 0
        self._plays = 0
    
    @property               # property for feed and plays
    def feeds(self):
        return self._feeds
    
    @property
    def plays(self):
        return self._plays
    
    def change_state(self,new_state):   # updates the puppy's state to the new state
        self._state = new_state
        self.reset()

    def throw_ball(self):               # calls the play method for whatever state the puppy is in
        return self._state.play(self)
    
    def give_food(self):
        return self._state.feed(self)   # calls feed method
    
    def inc_feeds(self):    # increments number of times puppy has been fed in a row
        self._feeds +=1

    def inc_plays(self):    # incrememnts number of times puppy has played in a row
        self._plays +=1

    def reset(self):        # reinitializes feeds and plays
        self._feeds = 0
        self._plays = 0