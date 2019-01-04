# Clase base de un nodo para el AST
class Node():

    # Metodo que retorna el resultado de evaluar el nodo
    def eval(self, env):
        raise NotImplemented()

    # Metodo que retorna la altura del nodo
    def height(self):
        raise NotImplemented()

    # Metodo que retorna una copia del nodo
    def copy(self):
        raise NotImplemented()

    # Metodo que retorna una lista con la operacion del nodo, su nodo izquierdo y el derecho
    def toList(self):
        raise NotImplemented()


