from src.AST.Node import Node

# Clase de un nodo con valor variable
class Variable(Node):
    def __init__(self, var):
        self.var = var

    def eval(self, env):
        return env.get(self.var)

    def height(self):
        return 1

    def copy(self):
        return self

    def toList(self):
        return [self]

    def __str__(self):
        return f"{self.var}"