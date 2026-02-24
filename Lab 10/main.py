# Lab 10
# Kamal Ali & William Nguyen
# 10/30/2024
# A game where a hero fights through a maze of monsters

import check_input
from hero import Hero
from map import Map
from enemy import Enemy
import random

def main():
    name = input('What is your name, traveler? ')
    map = Map()
    hero = Hero(name)
    finish = False

    while not finish and hero.hp > 0:
        print(str(hero))
        print(map.show_map(hero.loc))

        print('1. Go North')        # menu
        print('2. Go South')
        print('3. Go East')
        print('4. Go West')
        print('5. Quit')

        choice = check_input.get_int_range('Enter a choice: ', 1, 5)
        if choice == 5:
            break       # quit
        
        map.reveal(hero.loc)

        if choice == 1:
            move = hero.go_north()
        elif choice == 2:
            move = hero.go_south()
        elif choice == 3:
            move = hero.go_east()
        else:
            move = hero.go_west()

        map.reveal(hero.loc)

        while True:
            if move == 'm':  # Monster tile
                monster = Enemy()
                print(f'You encounter a {monster.name}!')
                in_battle = True

                while in_battle:
                    print(f'1. Attack {monster.name}')
                    print('2. Run Away')
                    choice = check_input.get_int_range('Enter choice: ', 1, 2)

                    if choice == 1:
                        print(hero.attack(monster))
                        if monster.hp == 0:
                            print(f'You have slain the {monster.name}!')
                            map.remove_at_loc(hero.loc)
                            in_battle = False
                            break
                        else:
                            print(monster.attack(hero))

                    else:  # Run away
                        print('You ran away!')
                        direction = random.randint(1, 4)
                        if direction == 1:
                            new_move = hero.go_north()
                            print('You ran North!')
                        elif direction == 2:
                            new_move = hero.go_south()
                            print('You ran South!')
                        elif direction == 3:
                            new_move = hero.go_east()
                            print('You ran East!')
                        else:
                            new_move = hero.go_west()
                            print('You ran West!')

                        if new_move == 'o':  # hit wall
                            print('You hit a wall and the monster strikes you!')
                            print(monster.attack(hero))
                            if hero.hp == 0:
                                print('You have been defeated...')
                                return
                            continue  # stay in same battle
                        else:
                            move = new_move
                            map.reveal(hero.loc)
                            in_battle = False  # stop this fight, but continue outer loop
                if monster.hp == 0 or hero.hp == 0:
                    break

            elif move == 'o':
                print('You cannot go that way...')
                break
            elif move == 'n':
                print('There is nothing here...')
                break
            elif move == 's':
                print('You found your way back at the start of the dungeon.')
                break
            elif move == 'i':
                print('You found a Health Potion! You drink it to restore your health.')
                hero.heal()
                map.remove_at_loc(hero.loc)
                break
            elif move == 'f':
                print('Congratulations! You found the exit!')
                finish = True
                break
            else:
                break  # no new tile type

        print()

    print('Game Over')

if __name__ == "__main__":
    main()
