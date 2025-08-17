"""
    Classes should only implement interfaces (contract) they need.

    When classes only use interfaces they use:
    - Code is clear.
    - Behavior that is not needed is not implemented.
"""
from abc import abstractmethod, ABC


class Washer(ABC):
    @abstractmethod
    def wash(self):
        pass


class Drier(ABC):
    @abstractmethod
    def dry(self):
         pass


class MyWasher(Washer):
    def wash(self):
        print("Washing clothes 1")


class MyDrier(Drier):
    def dry(self):
        print("Dry clothes 1")


class MyWasherAndDrier(Washer, Drier):
    def wash(self):
        print("Washing clothes 2")

    def dry(self):
        print("Dry clothes 2")


my_washer = MyWasher()
my_drier = MyDrier()
my_washer_drier = MyWasherAndDrier()

my_washer.wash()
my_drier.dry()

my_washer_drier.wash()
my_washer_drier.dry()
