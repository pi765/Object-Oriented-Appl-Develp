# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# Turkey Decoration

import plate_decorator  # decorator

class Turkey(plate_decorator.PlateDecorator):
    def description(self):
        desc = super().description()                # all previous descriptions
        if "with" in desc:                          # ensure that there's only 1 "with in the string"
            return desc + " and Turkey"             # add turkey to the description
        else:
            return desc + " with Turkey"
    
    def area(self):
        return super().area() - 15                  # reduce area on plate by 15
    
    def weight(self):
        return super().weight() - 4                 # reduce weight capacity of plate by 4
    
    def count(self):
        return super().count() + 1                  # increment count