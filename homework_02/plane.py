"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_in):
        if self.cargo + cargo_in <= self.max_cargo:
            self.cargo = self.cargo + cargo_in
        else:
            raise CargoOverload("Cargo overload")

    def remove_all_cargo(self):
        temp_cargo = self.cargo
        self.cargo = 0
        return temp_cargo

# if __name__ == "__main__":
#     plane = Plane(1, 2, 3, 5)
#     plane.load_cargo(2)
