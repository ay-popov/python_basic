"""
create dataclass `Engine`
"""

from dataclasses import dataclass

@dataclass
class Engine:

     # volume1: int
     # pistons1: int
    def __init__(self, volume=1, pistons=1):
        self.volume = volume
        self.pistons = pistons
