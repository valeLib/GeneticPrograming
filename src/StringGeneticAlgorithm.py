from src.BitsGeneticAlgorithm import BitsGeneticAlgorithm

from src.Individual import Individual


class StringGeneticAlgorithm(BitsGeneticAlgorithm):

    def reproduction(self):
        newPopulation = []
        for _ in range(self.populationSize):
            a, b, *_ = self.random.choices(self.matingPool, k=2)
            mixingPoint = self.random.randint(1, self.numberOfGenes-1)
            newGenes = a.genes[:mixingPoint] + b.genes[mixingPoint:]
            newGenes = [i for i in newGenes]
            for i,val in enumerate(newGenes):
                if self.random.random() < self.mutationRate:
                    a, b, *_ = self.random.choices(self.poolList, k=2)
                    while newGenes[i] == a:
                        a, b, *_ = self.random.choices(self.poolList, k=2)
                    newGenes[i] = a
            newGenes = ''.join(newGenes)
            newPopulation += [Individual(newGenes)]
        self.population = newPopulation