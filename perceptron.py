import random

class Perceptron:

    def __init__(self, samples, exits, learning_rate =0.1, time=1000, limiar=-1):
        self.samples = samples
        self.exits = exits
        self.learning_rate = learning_rate
        self.time = time
        self.limiar = limiar
        self.n_samples = len(samples)
        self.n_attributes = len(samples[0])
        self.weight = []

    def degrau(self, u ):

        if (u >= 0):
            return  1
        else:
            return 0

    def train(self):

        for sample in self.samples:
            sample.insert(0, -1)

        for i in range(self.n_attributes):
            self.weight.append(random.random())

        self.weight.insert(0, self.limiar)
        n_time =0

        while True:

            error = False

            for i in range(self.n_samples):
                u = 0
                for j in range(self.n_attributes + 1):
                    u += self.weight[j] * self.samples[i][j]

                y = self.degrau(u) #obtem a saida da rede

                if (y != self.exits[i]):
                    #calcula o erro
                    error_aux = self.exits[i] - y
                    #faz o ajuste
                    for j in range(self.n_attributes + 1):
                        self.weight[j] = self.weight[j] + self.learning_rate * error_aux * self.samples[i][j]
                    error = True # erro ainda existe

            n_time += 1 #epoca incrementa 1



            if not error or n_time > self.time: #se o erro não existe, sair do loop
                break

    def test(self, sample):
        sample.insert(0, -1)
        u = 0
        for i in range(self.n_attributes + 1):
            u+= self.weight[i] * sample[i]

        y = self.degrau(u)

        print("Result : %d " %y)


samples = [[0,0], [0,1], [1,0], [1,1]]
exits_or = [0, 1, 1, 1]
exits_and = [0, 0, 0, 1]

entry = int(input("Choose your network: 1- Logic Gate Or / 2- Logic Gate And: "))


if (entry==1):

    network = Perceptron(samples, exits_or)

    network.train()

    network.test([0, 0])

    network.test([0, 1])

    network.test([1, 0])

    network.test([1, 1])


elif (entry==2):

    network = Perceptron(samples, exits_and)
    network.train()

    network.test([0, 0])

    network.test([0, 1])

    network.test([1, 0])

    network.test([1, 1])



