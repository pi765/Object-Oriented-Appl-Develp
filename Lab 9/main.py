# Lab 9
# Kamal Ali & William Nguyen
# 10/20/2024
# Try to escape a series of 3 random doors

from basic_door import BasicDoor
from locked_door import LockedDoor
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
import check_input
import random

def open_door(door):
    print(door.examine_door())  # display description of door
    print(door.menu_options())  # menu
    user_choice = check_input.get_int_range(f'Enter a number (1-{door.get_menu_max()}): ', 1, door.get_menu_max())  # get user selection
    print(door.attempt(user_choice))    # pass in user attempt to make an attempt
    while door.is_unlocked() == False:  # loop until attempt is successful
        print(door.clue())              # give a clue
        user_choice = check_input.get_int_range(f'Enter a number (1-{door.get_menu_max()}): ',1,door.get_menu_max())  # if the guess is wrong, ask the user again.
        print(door.attempt(user_choice))
    print(door.success())   # display success message
    
def main():
    print("Welcome to the Escape Room. You must unlock 3 doors to escape...\n")
    for i in range(3):  # loop 3 times
        door_choice = random.randint(1,4)   # randomly choose between 4 doors
        if door_choice == 1:
            door = BasicDoor()      # create door object
        elif door_choice == 2:
            door = LockedDoor()
        elif door_choice == 3:
            door = DeadboltDoor()
        else:
            door = ComboDoor()
        open_door(door)             # pass in door
        print()
    print("Congratulations! You escaped... this time.") # congratulatory message / game end

if __name__ == "__main__":
    main()