# Lab 8
# Kamal Ali & William Nguyen
# 10/14/2024
# inherit from Vehicle to create a Car class with a nitro boost special move

from vehicle import Vehicle
import random

class Car(Vehicle): # inherit Vehicle
    def special_move(self, obs_loc):
        if self.energy >= 15:      # if there is sufficient energy
            self.energy -= 15      # deduct 15 energy
            move = int(self._speed * 1.5) + random.randint(-1,1)    # move 1.5x speed +/-1

            if obs_loc is not None and self._position + move >= obs_loc:        # if there is an obstacle
                self._position = obs_loc                                        # set position to the obstacle
                print(f"{self._name} CRASHED into an obstacle!")
            else:
                self._position += move                                          # move the full distance
                print(f"{self._name} uses nitro boost and moves {move} units!")
        else:
            self._position += 1                                                     # out of energy, move 1
            print(f"{self._name} tried to use Nitro Boost but is all out of energy!")