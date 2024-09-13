
numRows = 5


def generatePascals():
    triangle = []
    for row in range(1, numRows + 1):
        if row == 1:
            triangle.append([1])
        elif row == 2:
            triangle.append([1, 1])
        else:
            row_gen = [1] + [0] * (row-2) + [1]
            for col in range(1, row - 1):
                row_gen[col] = triangle[row - 2][col - 1] + triangle[row - 2][col]
            triangle.append(row_gen)

    return triangle


pascal = generatePascals()

print(f"{pascal}")