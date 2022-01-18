import numpy as np
f = open("inputs.txt")

coordinates = list()
for line in f:
    #print("[{0},{1}] [{2},{3}]".format(line[0], line[2], line[7], line[9]))
    coordinates.append([list([line[0], line[2]]), list([line[7], line[9]])])


print(coordinates)
largest = max(coordinates)
largest = max(largest)
largest = max(largest)
board = np.zeros((int(largest) + 1, int(largest) + 1))

for coordinate in coordinates:
    x1 = int(coordinate[0][0])
    x2 = int(coordinate[1][0])
    y1 = int(coordinate[0][1])
    y2 = int(coordinate[1][1])
    # print("({0},{1}) , ({2},{3})".format(x1, y1, x2, y2))

    if x1 != x2:
        start = min(x1, x2)
        end = max(x1, x2)

        for start in range(end + 1):
            board[y1][start] = board[y2][start] + 1

    else:
        start = min(y1, y2)
        end = max(y1, y2)

        for start in range(end + 1):
            board[start][x1] = board[start][x2] + 1

print(board)



