from abc import ABC

from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight=1, fuel=4, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Low fuel, can't start")

    def move(self, distance):
         if self.fuel >= distance * self.fuel_consumption:
             self.fuel -= distance * self.fuel_consumption
             #self.fuel = 0
         else:
             raise NotEnoughFuel("Not enough fuel")

# if __name__ == "__main__":
#      vehicle = Vehicle(1,3,1)
#      vehicle.move(3)
#      print("1")





