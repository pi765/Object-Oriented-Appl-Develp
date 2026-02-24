# Lab 6
# Kamal Ali & William Nguyen
# 9/29/2024
# Calls Player object from player.py to play a game of Yahtzee

import check_input
from player import Player

def take_turn(player):
    player.roll_dice()      # roll the dice
    print(str(player))      # display the dice
    if player.has_three_of_a_kind() == True:    # check for any wins
        print("You got three of a kind!")
    elif player.has_pair() == True:
        print("You got a pair!")
    elif player.has_series() == True:
        print("You got a series of 3!")
    else:
        print("Aww.  Too Bad.")
    print("Score = ", player.points)    # display updated score
    

def main():
    print("- Yahtzee - ")
    player = Player()   # create a player object
    repeat = True
    while repeat == True:   # loop until player ends the game
        take_turn(player)
        repeat = check_input.get_yes_no("Play again? (Y/N): ")  # ask to repeat
        print()
    print("Game Over.")
    print("Final Score = ", player.points)  # display final points


if __name__ == "__main__":
    main()