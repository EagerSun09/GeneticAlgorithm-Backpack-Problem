from random import random
from random import randint
from copy import copy

# ----------------- NOTE---------------------
# If you want to change weight and value of box, do it in Genetic class
# The index of weight should matches the index of value (i.e. Weight[i]=Value[i])

class Genetic:
    # weight-> weight of every box
    # value-> the value of every box
    # limit-> capacity of the bag
    # population contains the possible solution(chromosome) for each generation
    # possibility contains the possibility of every chromosome being chosen to go through crossover
    # generationLimit is the number of generation
    # size is the number of population
    # mutation is the possibility of one chromosome go through mutation
    # best = the best case in each generation
    # best_ holds the best value in the best possible solutions
    weight = [20, 30, 60, 90, 50, 70, 30, 30, 70, 20, 20, 60]
    value = [6, 5, 8, 7, 6, 9, 4, 5, 4, 9, 2, 1]
    limit = 250
    population = []
    possibility = []
    generationLimit = None
    size = None
    mutation = None
    best = None
    best_ = None

    def __init__(self, generationLimit, size, mutation):
        self.generationLimit = generationLimit
        self.size = size
        self.mutation = mutation

    # First, generate a group of random solutions (chromosomes) as initial population.
    def initialPopulation(self):
        for i in range(self.size):
            init = []
            for j in range(len(self.weight)):
                r = random()
                init.append(round(r))
            self.population.append([init, self.fitness(init)])
        return True

    # Use a fitness function to simulate natural process
    # The fitness function is the total value of boxes in the bag now
    # Once the weight beyond the bag's limit, the result of fitness function will be 0
    def fitness(self, chromesome):
        weightSum = 0
        valueSum = 0
        for i in range(len(chromesome)):
            if chromesome[i] == 1:
                weightSum += self.weight[i]
                valueSum += self.value[i]
        if weightSum > self.limit:
            return 0
        else:
            return valueSum

    # We recognize the fittest individuals
    # Then cull half of the chromosomes that does not have a high fitness value.
    def findFitest(self):
        for i in range(len(self.population)):
            for j in range(i, len(self.population)):
                if self.population[i][1] < self.population[j][1]:
                    temp = self.population[i]
                    self.population[i] = self.population[j]
                    self.population[j] = temp
        self.population = self.population[:round(self.size / 2)]

    # We calculate the possibility of every individual to be selected based on their fitness result
    def getPossibility(self):
        self.possibility = []
        fsum = 0

        for i in self.population:
            fsum += i[1]

        afsum = 0
        for i in self.population:
            if fsum == 0:
                afsum = 0
            else:
                afsum += float(i[1] / fsum)

            self.possibility.append(afsum)

    # Using crossover and mutation to generate a new generation.
    def nextGeneration(self):

        crossoverResult = []

        for i in range(self.size - 1):
            r = random()
            for p in range(len(self.possibility)):
                if r < self.possibility[p]:
                    p1 = p
                    break

            r = random()
            for p in range(len(self.possibility)):
                if r < self.possibility[p]:
                    p2 = p
                    break

            crossoverResult.append(crossover(self.population[p1], self.population[p2]))

        self.population = []
        for i in crossoverResult:
            r = random()
            if r < self.mutation:
                newchro = mutation(i)
                self.population.append([newchro, self.fitness(newchro)])
        self.population.append(self.best)
        return True

    # We pick the best individual in the population and record the chromosome and its fitness value.
    def bestOne(self):
        maxi = []
        maxvalue = 0
        for i in self.population:
            if maxvalue < i[1]:
                maxvalue = i[1]
                maxi = i

        self.best = maxi
        self.best_ = maxvalue
        return True

    # Show the solution.
    def show(self):
        string1 = "We will choose: "
        string2 = "Each weight is:\t"
        string3 = "Each value is :  "
        weight = 0
        for i in range(len(self.weight)):
            if self.best[0][i] == 1:
                string1 += "Box" + str(i + 1) + "\t"
                string2 += str(self.weight[i]) + "\t\t"
                string3 += str(self.value[i]) + "\t\t"
                weight += self.weight[i]

        string2 = string2[:-1]
        string3 = string3[:-1]
        string4 = "Total weight is: "
        string4 += str(weight)
        string5 = "Total value is : " + str(self.best_)

        print(string1)
        print(string2)
        print(string3)
        print(string4)
        print(string5)

    # Execute algorithm
    def run(self):
        print("There are %d boxes." %len(self.weight))
        print("---------------------------------")
        print("Box Number\t Weight \t value")
        for i in range(int(len(self.weight))):
            print("\t\t%d \t\t %d\t\t\t %d" %(i+1, self.weight[i], self.value[i]))
        print("---------------------------------")
        self.initialPopulation()
        self.bestOne()
        for i in range(self.generationLimit):
            self.findFitest()
            self.getPossibility()
            self.nextGeneration()
            self.bestOne()
            # print(self.Best)

        self.findFitest()
        # print(self.Best)

        self.show()

# Use mutation to generate a new population.
def mutation(chromosome):
    chromosome = copy(chromosome)
    i = randint(0, len(chromosome) - 1)
    chromosome[i] = 1 - chromosome[i]
    return chromosome

# use crossover to generate a new population.
def crossover(chromosomeA, chromosomeB):
    i = randint(0, len(chromosomeA))
    chromosome = chromosomeA[0][:i] + chromosomeB[0][i:]
    return chromosome


if __name__ == "__main__":
    g = Genetic(200, 100, 0.5)
    g.run()