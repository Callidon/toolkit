#!/usr/bin/env python3
# Find solution for the Travelling salesman problem using a genetic algorithm
# Author : Thomas Minier

import argparse
import json
import math
import random
from city import City
from traveller import Traveller


def selection(population, sampleSize):
    newPopulation = list()
    # sort member by evaluation score
    sortedPopulation = sorted(population, key=lambda traveller: traveller.evaluatePath())
    return sortedPopulation[:sampleSize]


def reproduce(population, nbPartners):
    childrens = list()
    # each member breed with a random sample of travellers
    for traveller in population:
        partners = random.sample(population, nbPartners)
        childrens += [traveller.breed(partner) for partner in partners if traveller != partner]
    return childrens + population


def main():
    """Main function
    """
    parser = argparse.ArgumentParser(description='Find solution for the '
                                     'Travelling salesman problem using '
                                     'a genetic algorithm')
    parser.add_argument('-c', '--cities-file', type=str, required=True,
                        help='file which contains the data about cities')
    parser.add_argument('-p', '--population-size', type=str, required=True,
                        help='size of the population')
    parser.add_argument('-l', '--limit', type=str, required=True,
                        help='maximum number of generations')
    args = parser.parse_args()

    population = list()
    previousPopulation = list()
    threshold = int(args.population_size)

    # load cities from config file
    with open(args.cities_file, 'r') as data_file:
        json_cities = json.load(data_file)
    cities = [City.from_json(name, neighbours) for name, neighbours in json_cities.items()]

    # randomly generate first generation
    for n in range(int(args.population_size)):
        traveller = Traveller('Traveller{}'.format(random.random()))
        path = random.sample(cities, len(cities))
        for city in path:
            traveller.addCity(city)
        population.append(traveller)

    # perform algorithm until the population is stable between 2 generations
    nbIt = 0
    while (population != previousPopulation) and (nbIt <= int(args.limit)):
        previousPopulation = list(population)
        nbIt += 1
        # perform reproduction
        population = reproduce(population, math.ceil(len(population) / 2))
        # perform selection
        population = selection(population, threshold)

    print('Generation n°{}'.format(nbIt))
    print(['{} : {}'.format(traveller.id, traveller.evaluatePath()) for traveller in population])

if __name__ == "__main__":
    main()
