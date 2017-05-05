# encoding: utf-8
# Iterators

# в пайтан няма интерфейси

class SquaresUpTo(object):
    def __init__(self, up_to):
        self.up_to = up_to
        # self.i = 0
    
    def __iter__(self):
        self.i = 0 # тук за да можем да рестартираме стейта
        return self

    def next(self):
        if self.i < self.up_to:
            i = self.i
            self.i += 1
            return i ** 2
        else:
            raise StopIteration

# yield е нещо което стига до него, връща каквото му е зададено, но пази стейта до къде е стигнал, след викане 
# на метода next ще продължи от където е стигнал
def squares_up_to(up_to):
    for i in xrange(up_to):
        yield i ** 2

    for j in xrange(up_to):
        yield j + 1

# ultimate lists 
def extract_temperatures(records):
    for i in records:
        yield i[2]
# ... примера с температурите
if __name__ == '__main__':
    # sq = SquaresUpTo(100)
    # for s in sq:
    #     print s
    #     if s > 100:
    #         break

    # for s in sq:
    #     print s

    square1 = squares_up_to(10)
    print square1
    for sq in square1:
        print sq 