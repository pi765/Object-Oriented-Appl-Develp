# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# Green Bean decoration

import plate_decorator  # decorator

class GreenBeans(plate_decorator.PlateDecorator):
    def description(self):
        desc = super().description()            # all previous descriptions
        if "with" in desc:                      # ensure that there's only 1 "with in the string"
            return desc + " and Green Beans"    # add green beans to the description
        else:
            return desc + " with Green Beans"
    
    def area(self):
        return super().area() - 20              # reduce area on plate by 20
    
    def weight(self):
        return super().weight() - 3             # reduce weight capacity of plate by 3
    
    def count(self):
        return super().count() + 1              # increment the count