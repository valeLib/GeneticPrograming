from src.AST.Node import Node

# Clase de un nodo con un valor numerico
class Value(Node):
    def __init__(self, val):
        self.val = val

    def eval(self, env):
        return self.val

    def height(self):
        return 1

    def copy(self):
        return self

    def toList(self):
        return [self]

    def __str__(self):
        return f"{self.val}"
