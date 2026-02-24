# Lab 7
# Kamal Ali & William Nguyen
# 10/8/2025
# Plays a game where a hero must defeat three dragons to complete the trial

import check_input
import random

from hero import Hero       # hero and dragon objects
from dragon import Dragon
from fire import FireDragon
from flying import FlyingDragon

def main():
    name = input("What is your name, challenger?\n")    # get hero's name
    hero = Hero(name,50)    # construct hero with 50 max hp
    dragons = [Dragon("Deadly Nadder", 10), FireDragon("Gronckle", 15), FlyingDragon("Timberjack", 20)]  # list of each of the dragons with their names and hp

    print(f"Welcome to dragon training, {name}\nYou must defeat 3 dragons.\n")

    while hero.hp != 0:     # loop until hero is defeated
        print(str(hero))                            # display hero name and hp

        for i in range(len(dragons)):                       # Display all attackable dragons
            print(i+1,". Attack ", dragons[i], sep= '')     # print the index of the dragon (+1) and the dragon's name and hp
        dragonChoice = check_input.get_int_range("Choose a dragon to attack: ",1,len(dragons))  # choose a dragon to attack
        dragonChoice -= 1                                                                       # match choice to the list position

        print("Attack with:")           # Display hero's attack choices
        print("1. Arrow (1 D12)")
        print("2. Sword (2 D6)")
        attackChoice = check_input.get_int_range("Enter weapon: ",1,2)  # attack choice
        if attackChoice == 1:
            hero.arrow_attack(dragons[dragonChoice])    # attack with arrow
        else:
            hero.sword_attack(dragons[dragonChoice])    # attack with sword
        if dragons[dragonChoice].hp == 0:                                   # when dragon has 0 hp
            print(f"You defeated the {dragons[dragonChoice].name}!")
            dragons.pop(dragonChoice)                                       # remove dragon from the list
        if not dragons:
            print("\nCongratulations! You have defeated all 3 dragons, you have passed the trials.")    # end loop when list is empty
            break

        attackingDragon = random.randint(1,len(dragons)) - 1    # get a random index in dragons list
        dragonAttack = random.randint(1,2)                      # randomly choose the dragon's attack: 1 or 2 (1 for basic attack, 2 for special)
        if dragonAttack == 1:
            dragons[attackingDragon].basic_attack(hero)         # basic attack
            print()
        else:
            dragons[attackingDragon].special_attack(hero)       # special attack
            print()
        if hero.hp == 0:
            print("Challenge failed. Hero is knocked out.")     # fail condition

if __name__ == "__main__":
    main()