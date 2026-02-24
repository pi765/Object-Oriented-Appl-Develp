# Lab 14
# Kamal Ali & William Nguyen
# 12/03/2025
# A sleepy puppy simulator that you can feed and throw a ball

from puppy import Puppy
import check_input
def main():
    print("Congratulations on your new puppy!")
    puppy = Puppy()     # create a puppy
    choice = 0
    while choice != 3:  # loop until quit
        print("What would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")
        choice = check_input.get_int_range("Enter choice: ",1,3)
        print()

        if choice == 1:
            print(puppy.give_food())    # try to get puppy to eat
        elif choice == 2:
            print(puppy.throw_ball())   # try to get puppy to play

if __name__ == "__main__":
    main()