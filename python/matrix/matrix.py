class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")

    def row(self, index):
        return [int(item) for item in self.matrix_string[index-1].split(' ')]

    def column(self, index):
        return [int(item.split(' ')[index-1]) for item in self.matrix_string]
