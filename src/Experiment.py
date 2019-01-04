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
        fitnessGenerations += [mean_fitness]
        generations += 1
        if best_score == None or algorithm.population[0].score < best_score:
            best_score = algorithm.population[0].score
            if best_score == algorithm.population[0].score:
                equal_score += 1

        if best_score == 0 or equal_score > 4:
            break
        algorithm.reproduction()

    return generations

def experimentAST():
    sizes = [6, 7, 8, 9, 10]
    operators = [operator.add, operator.sub, operator.mul]
    terminals = [19, 7, 40, 3]
    generations = []
    for s in sizes:
        tmp = []
        for _ in range(5):
            algorithm = GeneticPrograming(mutationRate, 500, s, operators, terminals, 147)
            g = main(algorithm)
            tmp += [g]
        tmp = np.array(tmp)
        generations += [np.mean(tmp)]

    lineChart(sizes, generations, "Altutra máxima", "Número de generaciones",
              "Generaciones por altura")

if __name__ == '__main__':
    experimentAST()