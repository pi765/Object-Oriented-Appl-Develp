# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# Interface for SmallPlate and LargePlate components and PlateDecorator

import abc
class Plate(abc.ABC):       # plate interface
    @abc.abstractmethod
    def description(self):  # returns description: str
        pass

    @abc.abstractmethod     # returns area: int
    def area(self):
        pass
    
    @abc.abstractmethod
    def weight(self):       # returns weight: int
        pass

    @abc.abstractmethod
    def count(self):        # returns count: int
        pass