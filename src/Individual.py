
class Individual():
    def __init__(self, AST):
        self.AST = AST
        self.score = 0

    def __str__(self):
        return str(self.AST)