import random

from src.Charts import lineChart
from src.NQueenGeneticAlgorithm import NQueenGeneticAlgorithm

if __name__ == '__main__':
    mutationRate = 0.1
    populationSize = 5000
    numberOfGenes = 12

    algorithm = NQueenGeneticAlgorithm(mutationRate, populationSize, numberOfGenes, None, random.Random())
    algorithm.generatePopulation()

    generations = 0
    fitnessGenerations = []
    while True:
        algorithm.evaluateFitness(None)
        algorithm.selection()
        fitnessGenerations += [algorithm.population[0].score]
        generations += 1
        if algorithm.population[0].score == 0:
            print(algorithm.population[0].genes)
            break
        algorithm.reproduction()

    lineChart(list(range(generations)), fitnessGenerations, "Número Generaciones", "Fitness promedio", "N-queen")