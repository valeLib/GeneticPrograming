from src.Individual import Individual

class BitsGeneticAlgorithm():
    def __init__(self, mutationRate, populationSize, numberOfGenes, pool, random):
        self.mutationRate = mutationRate
        self.populationSize = populationSize
        self.numberOfGenes = numberOfGenes
        self.poolList = list(pool)
        self.matingPool = []
        self.population = []
        self.random = random

    def generatePopulation(self):
        population = []
        for i in range(self.populationSize):
            genes = ''
            for j in range(self.numberOfGenes):
                genes += self.random.choice(self.poolList)
            individual = Individual(genes)
            population += [individual]
        self.population = population

    def evaluateFitness(self, expected):
        for individual in self.population:
            count = 0
            for i,j in zip(individual.genes, expected):
                if i != j:
                    count += 1
            individual.score = count

    def selection(self):
        self.population.sort(key = lambda x: x.score)
        self.matingPool =  self.population[:self.populationSize//4]

    def reproduction(self):
        newPopulation = []
        for _ in range(self.populationSize):
            a, b, *_ = self.random.choices(self.matingPool, k=2)
            mixingPoint = self.random.randint(1, self.numberOfGenes-1)
            newGenes = a.genes[:mixingPoint] + b.genes[mixingPoint:]
            newGenes = [i for i in newGenes]
            for i,val in enumerate(newGenes):
                if self.random.random() < self.mutationRate:
                    newGenes[i] = '1' if val == '0' else '0'
            newGenes = ''.join(newGenes)
            newPopulation += [Individual(newGenes)]
        self.population = newPopulation










