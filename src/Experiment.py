import random
import operator

import numpy as np

from src.Charts import lineChart
from src.GeneticPrograming import GeneticPrograming

mutationRate = 0.1

def main(algorithm):
    algorithm.generatePopulation()

    generations = 0
    equal_score = 0
    fitnessGenerations = []
    best_score = None
    while True:
        algorithm.evaluateFitness()
        fitness = list(map(lambda i: i.score, algorithm.population))
        mean_fitness = np.mean(fitness)
        algorithm.selection()
        if best_score == None or algorithm.population[0].score < best_score:
            best_score = algorithm.population[0].score
            if best_score == algorithm.population[0].score:
                equal_score += 1

        if best_score == 0 or equal_score > 4:
            break

        fitnessGenerations += [mean_fitness]
        generations += 1

    return generations

def experimentAST():
    sizes = [5, 8, 10, 11, 12, 13, 14, 15]
    operators = [operator.add, operator.sub, operator.mul]
    terminals = [19, 7, 40, 3]
    maxheight = 12
    generations = []
    for s in sizes:
        tmp = []
        for _ in range(5):
            algorithm = GeneticPrograming(mutationRate, s ** 2, s, operators, terminals, 147)
            g = main(algorithm)
            tmp += [g]
        tmp = np.array(tmp)
        generations += [np.mean(tmp)]

    lineChart(sizes, generations, "Altutra máxima", "Número de generaciones",
              "AST")

if __name__ == '__main__':
    experimentAST()