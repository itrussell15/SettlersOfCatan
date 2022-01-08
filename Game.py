# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 00:41:47 2022

@author: Schmuck
"""

class Game:
    
    def __init__(self):
        self.board = Board()
        self.players = []
        
    def addPlayer(self, name):
        self.players.append(Player(name))
        
    def getPlayer(self, name):
        for p in self.players:
            if (p.name == name.lower()):
                return p
        
    def rollDice(self):
        val = random.randint(2, 12)
        print("Dice Rolled: {}".format(val))
        self._cardCollection(val)
    
    def _cardCollection(self, val):
        for t in self.board.tiles:
            if t.rollValue == val and t.resource != Resource.DESERT:
                for v in t.vertices:
                    print(v)
                    if v.structure:
                        v.structure.owner.hand.add(
                            t.resource,
                            v.structure.type.value)
                        
class Board:
    
    def __init__(self, shape = (3, 4, 5, 4, 3),
                 resources = {Resource.ORE: 3,
                              Resource.WOOD: 4,
                              Resource.SHEEP: 4,
                              Resource.DESERT: 1,
                              Resource.BRICK: 3,
                              Resource.WHEAT: 4},
                 rollVal = {2: 1,
                            3: 2,
                            4: 2,
                            5: 2,
                            6: 2,
                            8: 2,
                            9: 2,
                            10: 2,
                            11: 2,
                            12: 1}
                 ):
        self.tiles, self.vertices = self._create(shape, resources, rollVal)

    def _create(self, shape, resources, values):
        return self._selectHelper(shape, resources, values)
    
    def _selectHelper(self, shape, resources, values):
        tiles = set()
        vertices = {}
        for n, i in enumerate(shape):
            for j in range(i):
                r, resources = self._selectResource(resources)
                if r != Resource.DESERT:
                    v, values = self._selectResource(values)
                else:
                    v = 0
                t = self.Tile([n, j], r, v)
                vertices = self._manageVertices(vertices, t)
                tiles.add(t)
        vertices = self._CreateVertices(vertices)

        return tiles, vertices
    
    def _CreateVertices(self, vertices):
        return [self.Vertex(v, tuple(vertices[v])) for v in vertices]
    
    def _manageVertices(self, vertices, tile):
        for v in tile.vertices:
            if v in vertices:
                vertices[v].append(tile)
            else:
                vertices[v] = [tile]
        return vertices
    
    def _selectResource(self, r):
        selection = list(r.keys())[random.randint(0, len(r.keys())-1)]

        if (r[selection] > 0):
            r[selection] = r[selection] - 1
            return selection, r
        else:
            return self._selectResource(r)
    
    def print(self):
        for tile in self.tiles:
            print(tile)

    def printVertices(self):
        for v in self.vertices:
            print(v)

    class Tile:
        
        def __init__(self, location, resource, rollVal):
            
            self.location = location
            self.resource = resource
            self.rollValue = rollVal
            self.isBlocked = False
            self.vertices = self.tile_vertices(location[0], location[1])
            
        def __str__(self):
            return "Tile(location = {}, resource = {}, value = {})".format(
                self.location,
                self.resource.name,
                self.rollValue)
                    
        # Vertices Format = (row, column)
        def tile_vertices(self, row, col):
            points = set()
            p_row = row*2
            for i in range(0, 4):
                if i == 1 or i == 2:
                    points.add((p_row+i, col))
                    points.add((p_row+i, col+1))
                else:
                    points.add((p_row+i, col))
            # TODO solve how to return Vertex() instead of a tuple
            return tuple(sorted(points))
        
    class Vertex:
        
        def __init__(self, location, tiles):
            self.structure = None
            self.location = location
            self.resources = {t.resource: t.rollValue for t in tiles}
            self.tilesAttached = tiles
        
        def __str__(self):
            if not self.structure:
                out = "No struture"
            else:
                out = self.structure.type.name
            return "Vertex(location = ({}, {}), structure = {}, resources = {})".format(
                self.location[0],
                self.location[1],
                out, 
                {i.name : self.resources[i] for i in self.resources}
                )
            
        def build(self, build):
            self.structure = build     