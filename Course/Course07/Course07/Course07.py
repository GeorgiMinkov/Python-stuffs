# use psycho indexing from 1
# encoding: utf-8

class Vector(object):
    def __init__(self, *values):
        self._values = list(values) # за да може да е mutable


    def __getitem__(self, key):
       return self._values[key - 1]


    def __setitem__(self, key, value):
        self._values[key - 1] = value


class Matrix(object):
    def __init__(self, rows, cols):
        # [0] * 3 = [0, 0, 0]
        # става бъг, че при сетване на стойност я мултиплицира навсякъде заради умножението self._values = [[0] * cols] * rows
        self._values = [[0] * cols for i in xrange(0, rows)]

    def __getitem__(self, (row, column)):
        return self._values[row - 1][column - 1]

    def __setitem__(self, (row, column), value):
        self._values[row - 1][column - 1] = value



if __name__ == "__main__":
    #v = Vector(1, 5, 6)
    #v[1] = 9
    m = Matrix(3, 3)
    m[1, 2] = 10
   
    print m[1, 2]
    print m[2, 2]
    print m[3, 2]