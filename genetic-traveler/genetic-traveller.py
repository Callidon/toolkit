#!/usr/bin/env python3
# Find solution for the Travelling salesman problem using a genetic algorithm
# Author : Thomas Minier

import random
from city import City
from traveller import Traveller


def selection(population, sampleSize):
    newPopulation = list()
    populationSize = len(population)
    # sort member by evaluation score
    sortedPopulation = sorted(population, key=lambda traveller: traveller.evaluatePath())

    # take the best evaluated for the new population
    return sortedPopulation[:sampleSize]


def reproduce(population, nbPartners):
    newPopulation = list()
    # each member breed with a random sample of travellers
    for traveller in population:
        partners = random.sample(population, nbPartners)
        for partner in partners:
            # a traveller cannot breed with himself
            if traveller != partner:
                newPopulation.append(traveller.breed(partner))

    return newPopulation


def main():
    father = Traveller(1)
    mother = Traveller(2)
    nantes = City("Nantes")
    paris = City("Paris")
    lyon = City("Lyon")

    nantes.addNeighbour(paris, 10)
    nantes.addNeighbour(lyon, 20)
    paris.addNeighbour(nantes, 10)
    paris.addNeighbour(lyon, 30)
    lyon.addNeighbour(nantes, 20)
    lyon.addNeighbour(paris, 30)

    father.addCity(lyon)
    father.addCity(paris)
    father.addCity(nantes)

    mother.addCity(nantes)
    mother.addCity(lyon)
    mother.addCity(paris)

    print(father.evaluatePath())
    print(mother.evaluatePath())
    print(selection([mother, father], 1))

    children = father.breed(mother)
    # print(children.path)


if __name__ == "__main__":
    main()
