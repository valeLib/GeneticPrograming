
class Individual():
    def __init__(self, genes):
        self.genes = genes
        self.score = 0

    def __str__(self):
        return str(self.genes)