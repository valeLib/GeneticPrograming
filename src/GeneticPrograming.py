import itertools

from src.AST.Node import Node
from src.Individual import Individual
import random

from src.AST.Operation import Operation
from src.AST.Value import Value
from src.AST.Variable import Variable


class GeneticPrograming():
    def __init__(self, mutationRate, populationSize, maxheight, operators, terminals, expected):
        self.mutationRate = mutationRate
        self.populationSize = populationSize
        self.maxheight = maxheight
        self.operators = operators
        self.terminals = terminals
        self.expected = expected
        self.matingPool = []
        self.population = []

    def generateAST(self, height):
        if height == 0:
            return
        if height == 1:
            term = random.choice(self.terminals)
            if isinstance(term, str):
                node = Variable(term)
            else:
                node = Value(term)
            return node
        else:
            op = random.choice(self.operators)
            return Operation(op, self.generateAST(height-1), self.generateAST(height-1))

    def generatePopulation(self):
        population = []
        for i in range(self.populationSize):
            height = random.randint(1, self.maxheight)
            individual = Individual(self.generateAST(height))
            population += [individual]
        self.population = population

    def fitness(self, individual):
        predicted = individual.AST.eval({})
        individual.score = abs(self.expected - predicted)

    def evaluateFitness(self):
        for individual in self.population:
            self.fitness(individual)

    def selection(self):
        self.population.sort(key = lambda x: x.score)
        self.matingPool =  self.population[:self.populationSize//4]

    def mutation(self, node: Node):
        if isinstance(node, Value) or isinstance(node, Variable):
            new_terminal = random.choice(self.terminals)
            if random.random() < self.mutationRate:
                if isinstance(new_terminal, str):
                    return Variable(new_terminal)
                else:
                    return Value(new_terminal)
            return node
        if isinstance(node, Operation):
            new_operator = random.choice(self.operators)
            if random.random() < self.mutationRate:
                return Operation(new_operator, self.mutation(node.left), self.mutation(node.right))
            return Operation(node.op, self.mutation(node.left), self.mutation(node.right))

    def reproduction(self):
        newPopulation = []
        for _ in range(self.populationSize):
            a, b, *_ = random.choices(self.matingPool, k=2)
            AST_a = a.AST
            AST_b = b.AST
            combination_list = [self.operators, AST_a.toList(), AST_b.toList()]
            combination_list_rev = [self.operators, AST_b.toList(), AST_a.toList()]

            iterator = itertools.product(*combination_list)
            iterator_rev = itertools.product(*combination_list_rev)
            iterator_comb = itertools.chain(iterator, iterator_rev)

            best_score = None
            best_individual = None
            for iter in iterator_comb:
                AST = Operation(iter[0], iter[1], iter[2])
                height = AST.height()
                individual = Individual(AST)
                self.fitness(individual)

                if (best_score == None or individual.score < best_score) and height < self.maxheight:
                    best_score = individual.score
                    best_individual = individual
            #Mutation
            if random.random() < self.mutationRate:
                best_individual.AST = self.mutation(best_individual.AST)

            newPopulation += [best_individual]
            self.population = newPopulation

    #Mutacion:
    # si es terminal -> lanzo moneda y permuto por cualquier terminal
    # si op: lanzo moneda y si hay mutacion muto la operacion recursivamente

    #Maiting:
    #convinaciones posibles entre [ops] [a, a_l, a_r] [b, b_l, b_r]
    #y usar el con mejor score y con altura menor a altura maxima










