#!/usr/bin/env python3
# Exercice with a neural network which learn to use logical operators
# Author : Thomas Minier
import argparse
import json
import sys


def main():
    """Main function
    """
    parser = argparse.ArgumentParser(description='Small neurla network with one layer ')
    parser.add_argument('-t', '--training-set', type=str, required=True,
                        help='file which contains the training set')
    parser.add_argument('-l', '--learning-rate', type=str, required=True,
                        help='the learning rate, must be in [0.0, 1.0[')
    args = parser.parse_args()

    iterationCount = 1
    threshold = 1
    learningRate = float(args.learning_rate)
    weights = [0.0, 0.0]
    with open(args.training_set, 'r') as data_file:
        trainingSet = json.load(data_file)

    # if incorrect learning rate
    if (learningRate < 0.0) or (learningRate >= 1.0):
        sys.exit('Error : The learning rate must be bigger than 0.0 and strictly lesser than 1.0')

    # learning loop
    while True:
        print('# ------------------- #')
        print('> Iteration n°{}'.format(iterationCount))

        errorCount = 0

        for key, datas in trainingSet.items():
            print('Current training data : {}'.format(key))
            # compute the weighted sum
            weightedSum = 0
            for ind in range(len(datas['inputs'])):
                weightedSum += datas['inputs'][ind] * weights[ind]

            # biais output
            output = 0
            if weightedSum >= threshold:
                output = 1

            print('Expected output : {}'.format(datas['output']))
            print('Current output : {}'.format(output))

            # compute error factor
            error = datas['output'] - output
            if error != 0:
                errorCount += 1

            # adjuste weights for next iteration
            for ind in range(len(datas['inputs'])):
                weights[ind] += learningRate * error * datas['inputs'][ind]

            print('New weights : {}'.format(weights))

        # no error means that the learning is a success
        if errorCount == 0:
            break
        else:
            iterationCount += 1
            print('{} errors during current iteration. Starting a new training iteration'.format(errorCount))

    print('# ------------------- #')
    print('Learning done. Final weights : {}'.format(weights))

if __name__ == "__main__":
    main()
