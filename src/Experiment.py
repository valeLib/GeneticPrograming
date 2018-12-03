import random

import numpy as np

from src.BitsGeneticAlgorithm import BitsGeneticAlgorithm
from src.Charts import lineChart
from src.NQueenGeneticAlgorithm import NQueenGeneticAlgorithm
from src.StringGeneticAlgorithm import StringGeneticAlgorithm


def main(algorithm, word):
    algorithm.generatePopulation()

    generations = 0
    fitnessGenerations = []
    while True:
        algorithm.evaluateFitness(word)
        fitness = list(map(lambda i: i.score, algorithm.population))
        mean_fitness = np.mean(fitness)
        algorithm.selection()
        if algorithm.population[0].score == 0:
            print(algorithm.population[0].genes)
            break
        algorithm.reproduction()

        fitnessGenerations += [mean_fitness]
        generations += 1

    return generations

def experimentBits():
    sizes = [5, 8, 10, 11, 12, 13, 14, 15]
    generations = []
    for s in sizes:
        tmp = []
        for _ in range(5):
            algorithm = BitsGeneticAlgorithm(0.1, s ** 2, s, '01', random.Random())
            word = ''
            for j in range(s):
                word += random.choice('01')
            g = main(algorithm, word)
            tmp += [g]
            print(s)
        tmp = np.array(tmp)
        generations += [np.mean(tmp)]
    lineChart(sizes, generations, "Tamaño de secuencia", "Número de generaciones", "Secuencia de Bits")

def experimentString():
    sizes = [5, 8, 10, 11, 12, 13, 14, 15]
    generations = []
    for s in sizes:
        tmp = []
        for _ in range(5):
            algorithm = StringGeneticAlgorithm(0.1, s ** 2, s, 'abcdefghijklmnñopqrstuvwxyz', random.Random())
            word = ''
            for j in range(s):
                word += random.choice('abcdefghijklmnñopqrstuvwxyz')
            g = main(algorithm, word)
            tmp += [g]
            print(s)
        tmp = np.array(tmp)
        generations += [np.mean(tmp)]

    lineChart(sizes, generations, "Tamaño de string", "Número de generaciones", "Secuencia de caracteres")


def experimentNQueen():
    sizes = [5, 8, 10, 11, 12, 13, 14, 15]
    generations = []
    for s in sizes:
        tmp = []
        for _ in range(5):
            algorithm = NQueenGeneticAlgorithm(0.1, s ** 2, s, None, random.Random())
            g = main(algorithm, None)
            tmp += [g]
            print(s)
        tmp = np.array(tmp)
        generations += [np.mean(tmp)]

    lineChart(sizes, generations, "Tamaño del tablero", "Número de generaciones",
              "N Reinas")

if __name__ == '__main__':
    #experimentBits()
    #experimentString()
    experimentNQueen()
