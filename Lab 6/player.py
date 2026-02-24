# Lab 6
# Kamal Ali & William Nguyen
# 9/29/2024
# Create a Player object that makes a list of 3 Die objects that can check if there is any wins for a game of Yahtzee

from die import Die
class Player:
    def __init__(self):
        self._die = [Die(),Die(),Die()]     # list of 3 die objects
        self._die.sort()                    # sort the list
        self._points = 0                    # initialize points to 0

    @property               # getter decorator
    def points(self):
        return self._points
    
    def roll_dice(self):
        for dice in self._die:  # loop through each die in the dice list
            dice.roll()         # roll each die
        self._die.sort()        # sort the list

    def has_pair(self):
        if self._die[0] == self._die[1] or self._die[0] == self._die[2] or self._die[1] == self._die[2]:    # check if any die values are the same
            self._points += 1   # increment points by 1
            return True
    
    def has_three_of_a_kind(self):
        if self._die[0] == self._die[1] == self._die[2]:    # check if the values are the same
            self._points += 3   # increment points by 3
            return True

    def has_series(self):
        if self._die[2] - self._die[1] == 1 and self._die[1] - self._die[0] == 1: # check if the values in the dice are in a series
            self._points += 2   # increment points by 2
            return True
    
    def __str__(self):
        return f"D1={self._die[0]}, D2={self._die[1]}, D3={self._die[2]}"   # return a string
    