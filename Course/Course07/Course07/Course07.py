# use psycho indexing from 1
# encoding: utf-8

class Vector(object):
    def __init__(self, *values):
        self._values = list(values) # ?? ?? ???? ?? ? mutable


    def __getitem__(self, key):
       return self._values[key - 1]


    def __setitem__(self, key, value):
        self._values[key - 1] = value


class Matrix(object):
    def __init__(self, rows, cols):
        # [0] * 3 = [0, 0, 0]
        # ????? ???, ?? ??? ??????? ?? ???????? ? ???????????? ????????? ?????? ??????????? self._values = [[0] * cols] * rows
        self._values = [[0] * cols for i in xrange(0, rows)]

    def __getitem__(self, (row, column)):
        return self._values[row - 1][column - 1]

    def __setitem__(self, (row, column), value):
        self._values[row - 1][column - 1] = value


def f(*args):
    print args


class Rapper(object):
    def __init__(self, func):
       self.func = func

    def __call__(self, *args):
        return map(self.func, args)

def sqare(x):
    return x ** 2

#######################################################################
def wrapWith(f):
    def wrapper(g):
        def wrapped(*args, **kwargs):
            return f(g(*args, **kwargs))
        return wrapped
    return wrapper

def kasa(f):
    print "KASA"

@wrapWith(kasa)
def bira():
    print "bira"
    return 42


class WrapWith(object):
    def __init__(self, f):
        self.f = f
    
    def __call__(self, g):
        def wrapped(*args, **kwargs):
            return self.f(g(*args, **kwargs))
        return wrapped

########################inheritance
class D(object):
    def foo(self):
        print "D's foo"


class C(D):
    def foo(self):
        print "C's foo"
        return super(C, self).foo()

class B(D):
    def foo(self):
        print "B's foo"
        return super(B, self).foo()

class A(B, C):
    def foo(self):
        print "A's foo"
        return super(A, self).foo()
    # MRO - Method Resolution Order
   
if __name__ == "__main__":
    #v = Vector(1, 5, 6)
    #v[1] = 9
    #m = Matrix(3, 3)
    #m[1, 2] = 10
   
    #print m[1, 2]
    #print m[2, 2]
    #print m[3, 2]

    #xs = [1, 2, 3]
    #f(xs)
    #f(*xs)

    #m = Rapper(sqare)
    #print m(1, 2, 3)

    #print bira()

    test = A()

    test.foo()
    print A.__mro__