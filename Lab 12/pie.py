# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# Pie Decoration

import plate_decorator  # decorator

class Pie(plate_decorator.PlateDecorator):
    def description(self):
        desc = super().description()        # all previous descriptions
        if "with" in desc:                  # ensure that there's only 1 "with in the string"
            return desc + " and Pie"        # add pie to the description
        else:
            return desc + " with Pie"
    
    def area(self):
        return super().area() - 19          # reduce area on plate by 19
    
    def weight(self):
        return super().weight() - 8         # reduce weight capacity of plate by 8
    
    def count(self):
        return super().count() + 1          # increment count