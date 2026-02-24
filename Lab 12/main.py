# Lab 12
# Kamal Ali & William Nguyen
# 11/10/2024
# A game that has a user add food to their plate without going over the weight or area limit of a paper plate.

import check_input
from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie


def examine_plate(p):
    print(p.description())          # display description
    if p.weight() > 13:             # hint for how much weight the plate can hold
        print("Sturdiness: Strong")
    elif p.weight() >= 7:
        print("Sturdiness: Weak")
    elif p.weight() >= 1:
        print("Sturdiness: Bending")
    else:       # failure
        print("Your plate isn't strong enough for this weight of food! Your food spills onto the ground.")
        return True     # end loop

    if p.area() > 41:               # hint for how much area is left on plate
        print("Space available: Plenty")
    elif p.area() >= 21:
        print("Space available: Some")
    elif p.area() >= 1:
        print("Space available: Tiny bit")
    else:       # failure
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        return True     # end loop
    return False        # continue main loop

def main():
    print('- Thanksgiving Dinner -')
    print('Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!')
    print('Choose a plate:')
    print('1. Small Sturdy Plate\n2. Large Flimsy Plate')
    plateChoice = check_input.get_int_range('', 1, 2)       # select a Plate

    if plateChoice == 1:
        plate = SmallPlate()
    else:
        plate = LargePlate()
    
    quit = False

    while quit == False:            # loop until game end
        print('1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit')
        foodChoice = check_input.get_int_range('',1,6)     # select a Food

        if foodChoice == 1:         # add food to the plate
            plate = Turkey(plate)
        elif foodChoice == 2:
            plate = Stuffing(plate)
        elif foodChoice == 3:
            plate = Potatoes(plate)
        elif foodChoice == 4:
            plate = GreenBeans(plate)
        elif foodChoice == 5:
            plate = Pie(plate)
        else:                       # quit game
            examine_plate(plate)
            print(f'Good Job! You made it to the table with {plate.count()} items.')
            print(f'There was still {plate.area()} inches left on your plate.')
            print(f"Your plate could have held {plate.weight()} ounces of food.\nDon't worry, you can always go back for more. Happy Thanksgiving!")
            break

        quit = examine_plate(plate)

if __name__ == "__main__":
    main()