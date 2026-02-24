# Lab 14
# Kamal Ali & William Nguyen
# 12/03/2025
# Puppy asleep state, can be fed but not played with

from puppy_state import PuppyState

class StateAsleep(PuppyState):
    def play(self, puppy):      # return string
        return f"The puppy is asleep. It doesn't want to play right now."
    
    def feed(self, puppy):
        from state_eat import StateEat
        puppy.change_state(StateEat())  # puppy starts eating
        puppy.inc_feeds()               # +1 consecutive feeds
        return f"The puppy wakes up and comes running to eat."