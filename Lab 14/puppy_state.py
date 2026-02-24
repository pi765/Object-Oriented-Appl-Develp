# Lab 14
# Kamal Ali & William Nguyen
# 12/03/2025
# Interface for the puppy holding play and feed

import abc
class PuppyState:
    @abc.abstractmethod
    def play(self,puppy):   # abstract methods, used for the 3 States
        pass

    @abc.abstractmethod
    def feed(self,puppy):
        pass