from math import sqrt, pow

def distance(x: int, y: int) -> float: 
    return sqrt(pow(x, 2) + pow(y, 2))

print(distance(2, 1))
