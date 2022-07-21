import random

class CPerceptron:
    weights = [0] * 2
    def __init__(self):
        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(-1,1)
    def sign(self, n):
        if n >=0:
            return 1
        else:
            return -1

    def Guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += self.weights[i] * inputs[i]

        return self.sign(sum)

    def Train(self,inputs, label):
        error = label - self.Guess(inputs)
        for i in range (len(self.weights)):
            self.weights[i] += error * inputs[i] * 0.1



