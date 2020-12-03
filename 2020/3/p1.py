#!/usr/bin/env python3
import math
import numpy as np
from collections import namedtuple

infile = "input.txt"
with open(infile) as f:
    arr = np.array([list(line.strip()) for line in f])

class Cartesian:
    def __init__(self, x, y):
        self.x = x
        self.y = y

slope = Cartesian(x=3, y=1)
height, width = arr.shape[0], arr.shape[1]
num_moves = math.ceil(height / slope.y)
necessary_width = num_moves * slope.x
num_copies = math.ceil(necessary_width / width)

print("Original Input Shape: {}".format(arr.shape))
print("Num horizontal copies needed: {}".format(num_copies))
arr = np.tile(arr, num_copies)
height, width = arr.shape[0], arr.shape[1]
print("Duplicated Input Shape: {}".format(arr.shape))

num_trees = 0
position = Cartesian(x=0, y=0)
while position.x < width and position.y < height:
    point = arr[position.y, position.x]
    if point == "#":
        num_trees += 1

    position.x += slope.x
    position.y += slope.y

print("Number of trees hit: {}".format(num_trees))
