#!/usr/bin/env python3
import math
import numpy as np
from collections import namedtuple

def preprocess_input(filename, slope_x, slope_y):
    with open(filename) as f:
        arr = np.array([list(line.strip()) for line in f])

    height, width = arr.shape[0], arr.shape[1]
    num_moves = math.ceil(height / slope_y)
    necessary_width = num_moves * slope_x
    num_copies = math.ceil(necessary_width / width)

    print("Slope: ({}, {})".format(slope_x, slope_y))
    print("\tOriginal Input Shape: {}".format(arr.shape))
    print("\tNum horizontal copies needed: {}".format(num_copies))
    arr = np.tile(arr, num_copies)
    print("\tDuplicated Input Shape: {}".format(arr.shape))
    return arr

def compute_trees(filename, slope_x, slope_y):
    arr = preprocess_input(filename, slope_x, slope_y)
    num_trees = 0
    height, width = arr.shape[0], arr.shape[1]
    position_x, position_y = 0, 0 
    while position_x < width and position_y < height:
        point = arr[position_y, position_x]
        if point == "#":
            num_trees += 1

        position_x += slope_x
        position_y += slope_y

    return num_trees

if __name__ == "__main__":
    infile = "input.txt"
    slope_x, slope_y = 3, 1
    num_trees = compute_trees(infile, slope_x, slope_y)
    print("Number of trees hit: {}".format(num_trees))
