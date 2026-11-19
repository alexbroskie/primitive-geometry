from src.vector import Vector
from typing import List

def create_rect(origin : Vector, height : int | float, width : int | float):
    A = origin + Vector(-width/2, -height/2)
    B = origin + Vector(-width/2, height/2)
    C = origin + Vector(width/2, height/2)
    D = origin + Vector(width/2, -height/2)

    return [A, B, C, D]

def create_square(origin : Vector, side_len : int | float):
    return create_rect(origin, side_len, side_len)

def move(figure : List, dir : Vector, dist : int | float):
    move_vec = dir.unit() * dist
    figure = figure.copy()

    for i in range(len(figure)):
        figure[i] = figure[i] + move_vec

    return figure