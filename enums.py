# -*- coding: utf-8 -*-

from enum import Enum

class Resource(Enum):
    DESERT = 0
    WOOD = 1
    WHEAT = 2
    ORE = 3
    SHEEP = 4
    BRICK = 5
    
class StructureType(Enum):
    SETTLEMENT = 1
    CITY = 2