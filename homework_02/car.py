"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):
    engine = None

    def set_engine(self, engine_s: Engine):
        if isinstance(engine_s, Engine):
            self.engine = engine_s

        else:
            print("Type of the engine_s is wrong")

if __name__ == "__main__":
    car = Car(1,3,1)
    eng = Engine(1,1)
    car.set_engine(eng)

