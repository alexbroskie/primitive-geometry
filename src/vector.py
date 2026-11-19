class Vector:
    '''Describes a vector in 2D space'''
    x = 0,
    y = 0,

    def __init__(self, x : int | float = 0, y : int | float = 0):
        '''Creates (x, y) vector'''
        self.x = x
        self.y = y
    def __len__(self):
        '''Returns length of the vector'''
        return int((self.x**2 + self.y**2)**0.5)
    def __add__(self, other : Vector):
        return Vector(self.x+other.x, self.y+other.y)
    def __sub__(self, other : Vector):
        return Vector(self.x-other.x, self.y-other.y)
    def __mul__(self, other : int | float | Vector):
        if isinstance(other, (int, float)):
            return Vector(self.x*other, self.y*other)
        else:
            return self.x*other.x + self.y*other.y
    def __truediv__(self, scale : int | float):
        return Vector(self.x/scale, self.y/scale)
    def __eq__(self, other : Vector):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def unit(self):
        if len(self) == 0: return Vector()
        return self / len(self)