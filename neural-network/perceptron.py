

class Perceptron:

    def __init__(self, input, weight):
        self.input = input
        self.weight = weight

    def __repr__(self):
        return '<Perceptron : input = {} | weight = {} >'.format(self.input, self.weight)

    def compute(self):
        return self.input * self.weight

    def updateWeight(self, learningRate, errorRate):
        self.weight += learningRate * errorRate * self.input
