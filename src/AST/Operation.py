from src.AST.Node import Node

# Clase de un nodo con una operacion
class Operation(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def eval(self, env):
        return self.op(self.left.eval(env), self.right.eval(env))

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def copy(self):
        return Operation(self.op, self.left.copy(), self.right.copy())

    def toList(self):
        return [self, self.left, self.right]

    def __str__(self):
        return f"({self.left}{self.op}{self.right})"