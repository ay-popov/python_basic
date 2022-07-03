"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
     pass
    #print("LowFuelError")

class NotEnoughFuel(Exception):
     pass
    #print("NotEnoughFuel")
class CargoOverload(Exception):
    pass
    #print("CargoOverload")

