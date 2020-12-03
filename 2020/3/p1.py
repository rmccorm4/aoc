def solution(filename, slopes):
    with open(filename) as f:
        arr = [list(row.strip()) for row in f]
        height, width = len(arr), len(arr[0])
        print("Input (Height, Width): {}".format((height, width)))

    solutions = []
    for slope in slopes:
        num_trees = 0
        x, y = 0, 0
        slope_x, slope_y = slope[0], slope[1]
        while y < height:
            if arr[y][x] == "#":
                num_trees += 1

            x = (x + slope_x) % width
            y += slope_y

        solutions.append(num_trees)
        print("Slope: {} ---> Num Trees: {}".format(slope, num_trees))

    return solutions

if __name__ == "__main__":
    infile = "input.txt"
    slopes = [(3, 1)]
    print("Solution: {}".format(solution(infile, slopes)))
