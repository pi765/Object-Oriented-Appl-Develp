# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# Potatoes Decoration

import plate_decorator  # decorator

class Potatoes(plate_decorator.PlateDecorator):
    def description(self):
        desc = super().description()                # all previous descriptions
        if "with" in desc:                          # ensure that there's only 1 "with in the string"
            return desc + " and Potatoes"           # add potatoes to the description
        else:
            return desc + " with Potatoes"
    
    def area(self):
        return super().area() - 18                  # reduce area on plate by 19
    
    def weight(self):
        return super().weight() - 6                 # reduce weight capacity of plate by 6
    
    def count(self):
        return super().count() + 1                  # increment count