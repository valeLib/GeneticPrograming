from src.Charts import lineChart
from src.GeneticPrograming import GeneticPrograming
import operator

if __name__ == '__main__':
    mutationRate = 0.1
    populationSize = 500
    maxheight = 12

    operators = [operator.add, operator.sub, operator.mul]
    terminals = [19, 7, 40, 3]

    test = GeneticPrograming(mutationRate, populationSize, maxheight, operators, terminals, 147)

    test.generatePopulation()

    generations = 0
    equal_score = 0
    fitnessGenerations = []
    best_score = None
    while True:
        test.evaluateFitness()
        test.selection()
        fitnessGenerations += [test.population[0].score]
        generations += 1
        if best_score == None or test.population[0].score < best_score:
            best_score = test.population[0].score
            if best_score == test.population[0].score:
                equal_score += 1

        if best_score == 0 or equal_score > 4:
            break
        test.reproduction()

    lineChart(list(range(generations)), fitnessGenerations, "Número Generaciones", "Fitness promedio", "AST de operaciones y valores")
