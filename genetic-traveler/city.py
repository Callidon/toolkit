
class City:
    """Class which represent a city in the path of a traveller
    Author : Thomas Minier
    """

    def __init__(self, name):
        self.name = name
        self.neighbours = dict()

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return (self.name == other.name) and (self.neighbours == other.neighbours)

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return "<City : " + self.name + " | neighbours : " + str(self.neighbours) + ">"

    def addNeighbour(self, name, distance):
        self.neighbours[name] = distance

    def distanceWith(self, name):
        return self.neighbours[name]

    def from_json(name, neighbours):
        city = City(name)
        for neighbour_name, neighbour_distance in neighbours.items():
            city.addNeighbour(neighbour_name, float(neighbour_distance))
        return city
