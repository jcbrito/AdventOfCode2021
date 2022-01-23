import numpy as np
import re
f = open("inputs.txt")

coordinates = list()

for line in f:
    coordinates.append([int(s) for s in re.findall(r'\d+', line)])
print(coordinates)
largest = np.max(coordinates)

board = np.zeros((int(largest + 1), int(largest + 1)))

for coordinate in coordinates:
    x1 = int(coordinate[0])
    y1 = int(coordinate[1])
    x2 = int(coordinate[2])
    y2 = int(coordinate[3])

    if x1 == x2:

        start = min(y1, y2)
        end = max(y1, y2)

        for start in range(start, end + 1):
            board[start][x1] = board[start][x1] + 1

    elif y1 == y2:

        start = min(x1, x2)
        end = max(x1, x2)

        for start in range(start, end + 1):
            board[y1][start] = board[y1][start] + 1

# print(board)
count = 0
for x in board:
    count += len([i for i in x if i > 1])

print("Number of areas to avoid: {0}".format(count))



