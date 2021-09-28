
from sys import maxsize

class Project:
    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description


    def __repr__(self):
        return "%s:%s:" % (self.id, self.name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name


    def id_or_max(self): #  вычисляет по группе ключ, используемый для сравнения
        if self.id: # если у группы есть id
            return int(self.id)   # есть вероятность что id передастся как str
        else:
            return maxsize    # константа, озн максимальное число, кот может исп в списках (очень удобно на практике
                              # использовать его как максимальное число для последующей сортировки по возрастанию или убыванию)