# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# SmallPlate Component, holds the initial values and description

import plate
class SmallPlate(plate.Plate):
    def description(self):          # description of plate
        return f"Sturdy 10 inch paper plate"
    
    def area(self): # area of plate
        return 78
    
    def weight(self):   # weight capacity
        return 32
    
    def count(self):    # no items on plate
        return 0