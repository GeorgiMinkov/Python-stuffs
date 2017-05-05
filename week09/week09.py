# SUDOKU

class Sudoku(object):
    def __init__(self, str_data):
        self.size = 3
        self.table = {(i//(self.size**2), i%(self.size**2)): element for i, element in enumerate(str_data) if element != '.'} # string in hash map
        self.all_option = set(str(i) for i in xrange(1, self.size**2))

    def __getitem__(self, key):
        return self.table.get(key, None)

    def column(self, col):
        return [element for (i, j), element in self.table.iteritems() if j == col] # filter(lambda v: v is not None [self[i, col] for i in xrange(0, self.n**2)] )

    def row(self, r):
        return [element for (i, j), element in self.table.iteritems() if i == r] #
        # filter (lambda v: v is not None
        #  [self[r, j] for j in xrange(0, self.n**2)])

    def group(self, (r, c)):
        pass

    @property
    def is_solved(self):
        return len(self.table) == self.size**4

    def cell_option(self, r c):
        return self.all_option - (self.row(r) | self.column(c) | self.group)

    def solve(self):
        pass

# "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
if __name__ == '__main__':
    test =  Sudoku('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')

    