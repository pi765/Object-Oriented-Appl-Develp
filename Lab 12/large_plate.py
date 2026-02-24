# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# LargePlate Component, holds the initial values and description

import plate
class LargePlate(plate.Plate):
    def description(self):          # description of plate
        return f"Flimsy 12 inch paper plate"
    
    def area(self):         # area of plate
        return 113
    
    def weight(self):       # weight capacity
        return 24
    
    def count(self):        # no items on plate
        return 0