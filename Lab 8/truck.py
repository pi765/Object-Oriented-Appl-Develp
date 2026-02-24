# Lab 8
# Kamal Ali & William Nguyen
# 10/14/2024
# inherit from Vehicle to create a Truck class with a ram special move

from vehicle import Vehicle

class Truck(Vehicle):   # inherit Vehicle
    def special_move(self, obs_loc):
        if self.energy >= 15:  # if enough energy
            self.energy -= 15  # update energy
            move = self._speed * 2  # move at 2 times speed
            if obs_loc is not None and self._position + move >= obs_loc:    # if there is an obstacle
                self.position += move                                      # move the full distance
                print(f"{self._name} bashes through the obstacle and moves {move} units!")
            else:
                self.position += move                                      # move the full distance
                print(f"{self._name} rams forward {move} units!")
        else:
            self.position += 1         # move 1 position
            print(f"{self._name} tries to ram forward, but is all out of energy!")