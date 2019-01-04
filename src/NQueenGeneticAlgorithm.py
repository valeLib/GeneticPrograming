from src.GeneticPrograming import BitsGeneticAlgorithm

from src.Individual import Individual


class NQueenGeneticAlgorithm(BitsGeneticAlgorithm):
    def __init__(self, mutationRate, populationSize, numberOfGenes, pool, random):
        pool = list(range(0, numberOfGenes))
        super(NQueenGeneticAlgorithm, self).__init__(mutationRate, populationSize, numberOfGenes, pool, random)


    def generatePopulation(self):
        poolList = list(range(0, self.numberOfGenes))
        population = []
        for i in range(self.populationSize):
            new = [i for i in poolList]
            self.random.shuffle(new)
            individual = Individual(new)
            population += [individual]
        self.population = population

    def evaluateFitness(self, expected):
        for individual in self.population:
            count = 0
            for i in range(self.numberOfGenes):
                for j in range(i+1, self.numberOfGenes):
                    offx = abs(i-j)
                    offy = abs(individual.genes[i] - individual.genes[j])
                    if individual.genes[i] == individual.genes[j] or offx == offy:
                        count += 1
            individual.score = count

    def reproduction(self):
        newPopulation = []
        for _ in range(self.populationSize):
            a, b, *_ = self.random.choices(self.matingPool, k=2)
            newGenes = [-1]*self.numberOfGenes
            temp = []
            for i in range(self.numberOfGenes):
                if a.genes[i] == b.genes[i]:
                    newGenes[i] = a.genes[i]
                else:
                    temp += [a.genes[i]]
            self.random.shuffle(temp)
            for i in range(self.numberOfGenes):
                if newGenes[i] == -1:
                    newGenes[i] = temp[-1]
                    temp.pop()
            newPopulation += [Individual(newGenes)]
        self.population = newPopulation