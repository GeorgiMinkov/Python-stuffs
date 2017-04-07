import math

class Vector(object):
    def __init__(self, *args):
        if len(args) == 0 : self.val = (0, 0)
        else: self.val = args

    def norm(self): # Returns the norm (length, magnitude) of the vector
        return math.sqrt(sum(comp ** 2 for com in self))

    def normalize(self):
        norm = self.norm()
        return Vector(*(tuple(component / norm for component in self))) # * unpack-ва

    def __div__(self, coef):
        return Vector(*(tuple(component / coef for component in self)))

    def __sub__(self, other):
        return Vector(*(tuple(self_component - other_component for self_comtponent, 
        other_component in zip(self, other))))

    def __add__(self, other):
        return Vector(*(tuple(self_component + other_component for self_component,
        other_component in zip(self, other))))

    def __iter__(self):
        return self.val.__iter__()

    def __len__(self):
        return len(self.val)

    def __getitem__(self, key):
        return self.val[key]


