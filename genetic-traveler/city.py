# Class which represent a city in the path of a traveller
# Author : Thomas Minier

class City:

    def __init__(self, name):
        self.name = name
        self.neighbours = dict()

    def addNeighbour(self, name, distance):
        self.neighbours[name] = distance

    def distanceWith(self, name):
        if(name in self.neighbours):
            return self.neighbours[name]
        else:
            return None

    def __str__(self):
        return "[City : " + self.name + " | neighbours : " + str(self.neighbours) + "]"
