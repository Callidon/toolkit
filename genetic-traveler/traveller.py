import random


class Traveller:
    """Class which represent a travelling salesman
    Author : Thomas Minier
    """

    def __init__(self, id=None):
        self.id = id
        self.path = list()

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return self.path == other.path

    def __repr__(self):
        cities = [city.name for city in self.path]
        return '<Traveller : {}, cities : {}>'.format(self.id, cities)

    def addCity(self, city):
        self.path.append(city)

    def evaluatePath(self):
        """Evaluate the quality of the path taken by the traveller
        """
        pathLength = 0
        if len(self.path) > 0:
            previousCity = self.path[0]
            for ind in range(1, len(self.path)):
                pathLength += previousCity.distanceWith(self.path[ind].name)
                previousCity = self.path[ind]
        return pathLength

    def mutate(self):
        """Apply a mutation to the traveller
        """
        # swap two cities in the path
        first = random.randrange(len(self.path))
        second = random.choice([i for i in range(len(self.path)) if i != first])
        tmp = self.path[first]
        self.path[first] = self.path[second]
        self.path[second] = tmp

    def breed(self, partner, mutateChance=-1.0):
        """Breed two travellers and produce a new one
        """
        children = Traveller('Children{}'.format(random.random()))
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
        # try to mutate the children
        if random.random() >= mutateChance:
            children.mutate()
        return children
