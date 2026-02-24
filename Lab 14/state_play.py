# Lab 14
# Kamal Ali & William Nguyen
# 12/03/2025
# Puppy play state, can be played with but not fed, will go to sleep after 3 plays

from puppy_state import PuppyState

class StatePlay(PuppyState):
    def play(self, puppy):
        from state_asleep import StateAsleep
        puppy.inc_plays()       # +1 consecutive plays
        if puppy.plays >= 3:    # fall asleep at 3 plays
            puppy.change_state(StateAsleep())
            return f"You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"
        else:
            return f"You throw the ball again and the puppy excitedly chases it."

    def feed(self, puppy):      # return a string
        return f"The puppy is too busy playing with the ball to eat right now."