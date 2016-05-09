# Class which represent a travelling salesman
# Author : Thomas Minier

class Traveller:

    def __init__(self):
        self.path = list()

    def addCity(self, city):
        self.path.append(city)

    def evaluatePath(self):
        pathLength = 0
        previousCity = self.path[0]
        for city in range(1,len(self.path)):
            pathLength += previousCity.distanceWith(self.path[city])
            previousCity = city
        return pathLength

    def breed(self, partner):
        # TODO
        raise NotImplementedError
