# Lab 14
# Kamal Ali & William Nguyen
# 12/03/2025
# Puppy eat state, can be fed up to 3 times to go to sleep, and can be played with to change to the play state

from puppy_state import PuppyState

class StateEat(PuppyState):
    def play(self, puppy):
        from state_play import StatePlay
        puppy.change_state(StatePlay())     # change to play state
        puppy.inc_plays()                   # +1 consecutive plays
        return f"The puppy looks up from its food and chases the ball you threw."
    
    def feed(self, puppy):
        from state_asleep import StateAsleep
        puppy.inc_feeds()                   # +1 consecutive feeds
        if puppy.feeds >= 3:                # fall asleep at 3 feeds
            puppy.change_state(StateAsleep())
            return f"The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!"
        else:
            return f"The puppy continues to eat as you add another scoop of kibble to its bowl."