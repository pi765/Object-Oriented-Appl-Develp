# Lab 8
# Kamal Ali & William Nguyen
# 10/14/2024
# A game where the user chooses between a Car, Motorcycle, or Truck and races against the others, you may choose to go fast, slow, or use a special move with a limited amount of energy

import random
import check_input
from car import Car
from motorcycle import Motorcycle
from truck import Truck

def main():
    print("Rad Racer!")         # show menu
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('0') or else you'll crash!")
    print("1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special: Wheelie (2x speed, but might wipe out)")
    print("3. Behemoth Truck - a heavy truck. Speed: 6. Special: Ram (2x speed and it smashes through obstacles)")

    choice = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3) # get user choice between 1 and 3

    if choice == 1:       # create user's vehicle and opponent vehicles
        player = Car("Lightning Car", 'P', 7)   # player object
        vehicles = [player, Motorcycle("Swift Bike", 'M', 8), Truck("Behemoth Truck", 'T', 6)]  # list of vehicles
        player_lane = 0    # lane position
    elif choice == 2:
        player = Motorcycle("Swift Bike", 'P', 8)
        vehicles = [Car("Lightning Car", 'C', 7), player, Truck("Behemoth Truck", 'T', 6)]
        player_lane = 1
    elif choice == 3:
        player = Truck("Behemoth Truck", 'P', 6)
        vehicles = [Car("Lightning Car", 'C', 7), Motorcycle("Swift Bike", 'M', 8), player]
        player_lane = 2


    length = 100    # track length

    track = []  # 2d list for the track
    for i in range(3):
        lane = ['-' for _ in range(length)]     # create empty track in each lane

        spawnPositions = list(range(1, length - 1))     # obstacles can spawn anywhere except for start and finish
        obstacles = random.sample(spawnPositions,2)           # 2 obstacle positions with no duplicates

        for j in obstacles:
            lane[j] = '0'                   # place an obstacle at each obstacle position

        track.append(lane)                  # add lane to the 2d list

    finished = []       # list of finished racers

    for i in range(3):
        racer = vehicles[i]
        track[i][racer.position] = racer.initial       # place racer on the track

    while len(finished) < len(vehicles):            # loop until all racers are finished
        
        for racer in range(3):
            print(str(vehicles[racer]))     # print all racer stats
            
        for lane in track:
            print("".join(lane))        # display track

        if player not in finished:
            choice = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3) # get user movement choice
            print()
        previous_positions = [] # list of previous positions to mark with '*'
        for racer in vehicles:
            previous_positions.append(racer.position)   # mark the positions

        if player not in finished:  # player movement (when not finished)
            try:        # test to see if there is an obstacle
                next_obstacle = track[player_lane].index('0', player.position + 1)     # mark position of obstacle
            except:     # if not, return None
                next_obstacle = None

            if choice == 1:                         # player action
                player.fast(next_obstacle)
            elif choice == 2:
                player.slow(next_obstacle)
            elif choice == 3:
                player.special_move(next_obstacle)

        for i in range(3):      # opponent movement
            racer = vehicles[i]
            if racer in finished:
                continue        # stop moving when at the finish line
            if racer != player:
                try:    # check if there's an obstacle
                    next_obstacle = track[i].index('0', racer.position + 1)    # mark location of obstacle
                except:
                    next_obstacle = None    # no obstacle ahead

                if racer.energy <= 0:                   # when out of energy
                    racer.slow(next_obstacle)  # only move slowly
                else:
                    roll = random.randint(1, 10)    # random movement roll between 1 and 10
                    if roll <= 4:                   # 40% chance to go slow
                        racer.slow(next_obstacle)
                    elif roll <= 7:                 # 30% chance to go fast
                        racer.fast(next_obstacle)
                    else:                           # 30% chance to use special
                        racer.special_move(next_obstacle)
        print()

        for i in range(3):          # update track
            lane = track[i]
            racer = vehicles[i]

            prev = previous_positions[i]
            lane[prev] = '*'  # keep previous positions

            if racer.position >= length - 1:       # when past the finish line
                if racer not in finished:           # if not in the finished list
                    racer.position = length - 1     # place racer at the finish line
                    finished.append(racer)          # add racer to finished list
                racer.position = length - 1

            if 0 <= racer.position < length:            # place the initial (C,P,T,M) at the current position
                lane[racer.position] = racer.initial

            track[i] = lane     # update the lane
        

    for lane in track:          # final track display
        print("".join(lane))

    for placement in range(len(finished)):          # show final placements
        if placement == 0:
            print('1st place: ', str(finished[placement]))
        elif placement == 1:
            print('2nd place: ', str(finished[placement]))
        elif placement == 2:
            print('3rd place: ', str(finished[placement]))


if __name__ == "__main__":
    main()
