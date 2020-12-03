#!/usr/bin/env python3
import numpy as np
from p1 import compute_trees

if __name__ == "__main__":
    infile = "input.txt"
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    num_trees = [compute_trees(infile, slope[0], slope[1]) for slope in slopes]
    prod = np.prod(num_trees)
    for slope, trees in zip(slopes, num_trees):
        print("Slope: {}".format(slope))
        print("\tTrees hit: {}".format(trees))
    print("Product of trees hit: {}".format(prod))
