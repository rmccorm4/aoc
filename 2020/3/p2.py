from p1 import solution
from functools import reduce

if __name__ == "__main__":
    infile = "input.txt"
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = solution(infile, slopes)
    prod = reduce(lambda x,y: x*y, trees)
    print("Solution: {}".format(prod))
