# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# Decorator for food Decorations

import abc
import plate

class PlateDecorator(plate.Plate, abc.ABC):         # extends ABC and extends from Plate
    def __init__(self, p):                  # pass in p and assign it to _plate
        self._plate = p
    
    def description(self):                  # call each on _plate attribute
        return self._plate.description()
    
    def area(self):
        return self._plate.area()
    
    def weight(self):
        return self._plate.weight()
    
    def count(self):
        return self._plate.count()