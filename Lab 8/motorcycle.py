# Lab 8
# Kamal Ali & William Nguyen
# 10/14/2024
# inherit from Vehicle to create a Motorcycle class with a modified slow move and a wheelie special move

from vehicle import Vehicle
import random

class Motorcycle(Vehicle):  # inherit Vehicle
    def slow(self, obs_loc):        # override slow in vehicle
        move = int(self._speed * 0.75) + random.randint(-1,1)            # move at 0.75x speed +/-1 instead of the usual 0.5x +/-1
        if obs_loc is not None and self.position + move >= obs_loc:
            self.position += move
            print(f"{self._name} slowly dodges the obstacle and moves {move} units!")
        else:
            self.position += move
            print(f"{self._name} slowly moves {move} units!")
        
    def special_move(self, obs_loc):
        if self._energy >= 15:              # if vehicle has more than 15 energy
            self._energy -= 15              # deduct 15 energy
            if random.randint(1,100) < 75:      # 75 % chance of success
                move = int(self._speed * 2) + random.randint(-1,1)      # move at 2x speed +/-1
                if obs_loc is not None and self.position + move >= obs_loc:    # if there is an obstacle in the way
                    self.position = obs_loc                        # set position to the obstacle
                    print(f"{self._name} CRASHED into an obstacle!")
                else:
                    self.position += move                          # move the motorcycle
                    print(f"{self._name} pops a wheelie and moves {move} units!!")
            else:
                self.position += 1                                 # only move 1 space upon failure
                print(f"{self._name} fell over!")
        else:                                                       # no energy
            self.position += 1                                     # move 1 unit
            print(f"{self._name} tries to pop a wheelie, but is all out of energy!")