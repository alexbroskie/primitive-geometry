from src import rectangle

def perimeter(a : int | float):
    '''Returns a perimeter of a rectangle with "a" side'''
    return rectangle.perimeter(a, a)

def area(a : int | float):
    '''Returns an area of a square with "a" side'''
    return rectangle.area(a, a)