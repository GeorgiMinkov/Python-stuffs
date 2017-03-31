# encoding: UTF-8

import numbers
# import antigravity
import math

class Complex(object):
    def __init__(self, Re = 0, Im = 0):
        self.Re = Re
        self.Im = Im

    @property
    def norm(self):
        return math.sqrt(self.Re ** 2 + self.Im ** 2)

    @property
    def real(self):
        return self.Re
    
    @real.setter
    def real(self, new_re):
        self.Re = new_re

    def __radd__(self, other):
       return self.__add__(other)

    def __add__(self, other):
        if isinstance(other, numbers.Number): #  type(other) is numbers.Number:
            other = Complex(other, 0)
            
        return (Complex(self.Re + other.Re, self.Im + other.Im))
    
    def __str__(self):
        return "{Re} + i{Im}".format(Re = self.Re, Im = self.Im) # "{self.a + i{self.b}.format(self = self)}"

    def __rsub__(self, other):
        return self.__sub__(other) # self - other

    def __sub__(self, other):
        if isinstance(other, numbers.Number): # type(other) is numbers.Number:
            other = Complex(other, 0)

        return (Complex(self.Re - other.Re, self.Im - other.Im))
        
    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            other = Complex(other, 0)
        elif self.Re == 0 & self.Im == 1 & other.Re == 0 & other.Im == 1:
            return -1
        else:
            return Complex(self.Re*other.Re - self.Im*other.Im, self.Im*other.Re + self.Re*other.Im)
    
    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            other = Complex(other, 0)

        return self.Re == other.Re & self.Im == other.Im

    # def __getattr__(self, name):
    #     print "Niama: {}".format(name)
    #     return None

    # def __getattribute__(self, name): # винаги се вика когато се опитва да се чете
    #     print "I'm GOD : {}".format(name)

    #     return 42

    def __setattr__(self, name, value): # винаги се вика когато се опитва да се пише
        try: 
            if hasattr(self, name):
                object.__setattr__(self, name, value)
        except AttributeError as e: # как да направим наше изключение
            print "No attribute found {}".format(name)
""" 
create, add, substract, mult, devide, re, img, norm, print
equality, hash
"""    


if __name__ == "__main__":
    complex = Complex(1, 0)

    # print 6 - complex
    # print complex + 5.5
    # print complex * 6
    # print complex.real
    
    # complex.real = 5
    # print "Real " + str(complex.real)
    # print complex == complex
    # print complex.bira
    # print complex.real

    complex.bira = "kasa"