import random

from src.Charts import lineChart
from src.NQueenGeneticAlgorithm import NQueenGeneticAlgorithm

if __name__ == '__main__':
    algorithm = NQueenGeneticAlgorithm(0.1, 1000, 12, None, random.Random())
    algorithm.generatePopulation()

    generations = 0
    fitnessGenerations = []
    while True:
        algorithm.evaluateFitness(None)
        algorithm.selection()
        print(algorithm.population[0].score)
        fitnessGenerations += [algorithm.population[0].score]
        generations += 1
        if algorithm.population[0].score == 0:
            print(algorithm.population[0].genes)
            break
        algorithm.reproduction()

    lineChart(list(range(generations)), fitnessGenerations, "Número Generaciones", "Fitness promedio", "N-queen")