# Find solution for the Travelling salesman problem using a genetic algorithm
# Author : Thomas Minier

from city import City
from traveller import Traveller

def main():
    traveller = Traveller()
    nantes = City("Nantes")
    paris = City("Paris")
    nantes.addNeighbour(paris, 10)
    traveller.addCity(nantes)
    traveller.addCity(paris)
    print(traveller.evaluatePath())

if __name__ == "__main__":
    main()
