# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# Stuffing Decoration

import plate_decorator  # decorator

class Stuffing(plate_decorator.PlateDecorator):
    def description(self):
        desc = super().description()                # all previous descriptions
        if "with" in desc:                          # ensure only 1 "with"
            return desc + " and Stuffing"           # add stuffing to the description
        else:
            return desc + " with Stuffing"
    
    def area(self):
        return super().area() - 18                  # reduce area on plate by 18
    
    def weight(self):
        return super().weight() - 7                 # reduce weight capacity by 7
    
    def count(self):
        return super().count() + 1                  # increment count