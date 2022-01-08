# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:41:16 2022

@author: Schmuck
"""

class Structure:
    
    def __init__(self, vertex, thisType, owner):
        self.type = thisType
        self.vertex = vertex
        self.owner = owner
        
class Road:
    
    def __init__(self, a, b):
        pass