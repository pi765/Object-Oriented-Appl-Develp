# Lab 8
# Kamal Ali & William Nguyen
# 10/14/2024
# An abstract class with fast, slow, and special move functions

import random
import abc      # abstract

class Vehicle(abc.ABC):
    def __init__(self, name, initial, speed):   # initialize
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0  # starting position is 0
        self._energy = 100  # starting energy is 100

    @property                   # getters
    def initial(self):
        return self._initial
    
    @property
    def position(self):
        return self._position
    
    @property
    def energy(self):
        return self._energy
    
    @initial.setter                 # setters
    def initial(self, value):
        self._initial = value

    @position.setter
    def position(self, value):
        self._position = value
    
    @energy.setter
    def energy(self,value):
        self._energy = value
    
    def fast(self, obs_loc):
        if self.energy >= 5:   # if the vehicle has more than 5 energy
            self.energy -= 5   # remove 5 energy
            move = self._speed + random.randint(-1,1)   # move at 1x speed +/-1
            if obs_loc is not None and self.position + move >= obs_loc:    # if there is an obstacle in the way
                self.position = obs_loc                                    # set position to the obstacle's
                print(f"{self._name} CRASHED into an obstacle!")
            else:
                self._position += move                                      # else, move at full speed
                print(f"{self._name} quickly moves {move} units!")
        else:
            self._position += 1                                             # move 1 unit if no energy
            print(f"{self._name} had low energy and moved slowly 1 space.")

    def slow(self, obs_loc):
        move = int(self._speed / 2) + random.randint(-1,1)              # move at half speed +/-1
        if obs_loc is not None and self.position + move == obs_loc:
            self.position += move                                      # drive past the obstacle, moving full distance
            print(f"{self._name} slowly dodges the obstacle and moves {move} spaces!")
        else:
            self.position += move                                      # move the full distance
            print(f"{self._name} slowly moves {move} units!")

    def __str__(self):
        return f"{self._name} [Position - {self.position}, Energy - {self.energy}]" # return a strong of name, position, energy

    @abc.abstractmethod                 # abstract method, overriden in subclasses
    def special_move(self, obs_loc):
        pass