# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:40:05 2022

@author: Schmuck
"""

class Player:
    
    def __init__(self, name):
        self.points = 0
        self.name = name.lower()
        self.hand = self.Hand()
        self.structures = []
        self.roads = []
        self.devCards = []
        
    def __str__(self):
        return "Player(name = {}, points = {})".format(self.name.title(), self.points)
    
    def buildStructure(self, vertex, thisType):
        s = Structure(vertex, thisType, self)
        self.structures.append(s)
        vertex.build(s)
        
    class Hand:
        
        def __init__(self):
            self.numCards = 0
            self.cards = []
            
        def addCards(self, resource, number):
            for i in range(number):
                self.cards.append(resource)
                self.numCards +=1
        
        def removeCards(self):
            pass