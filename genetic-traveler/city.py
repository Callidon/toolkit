
class City:
    """Class which represent a city in the path of a traveller
    Author : Thomas Minier
    """

    def __init__(self, name):
        self.name = name
        self.neighbours = dict()

    def __eq__(self, other):
        return (self.name == other.name) and (self.neighbours == other.neighbours)

    def __hash__(self):
        return hash(self.name)

    def addNeighbour(self, name, distance):
        self.neighbours[name] = distance

    def distanceWith(self, name):
        if(name in self.neighbours):
            return self.neighbours[name]
        else:
            return None

    def __repr__(self):
        return "<City : " + self.name + " | neighbours : " + str(self.neighbours) + ">"
