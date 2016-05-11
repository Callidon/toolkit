import random

class Traveller:
    """Class which represent a travelling salesman
    Author : Thomas Minier
    """

    def __init__(self):
        self.path = list()

    def __eq__(self, other):
        return self.path == other.path

    def addCity(self, city):
        self.path.append(city)

    def evaluatePath(self):
        """Evaluate the quality of the path taken by the traveller
        """
        pathLength = 0
        previousCity = self.path[0]
        for city in range(1,len(self.path)):
            pathLength += previousCity.distanceWith(self.path[city])
            previousCity = city
        return pathLength

    def breed(self, partner):
        """Breed two travellers and produce a new one
        """
        children = Traveller()
        # take a sample city sequence from self
        locustInd = random.randint(0, len(self.path))
        locust = self.path[0:locustInd]
        ind = 0
        # fill the path of children with fragments of the parents' paths
        for city in partner.path:
            if (ind <= len(locust)) and (city in locust):
                children.addCity(locust[ind])
                ind += 1
            else:
                children.addCity(city)
        return children
