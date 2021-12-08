import numpy as np


def check_number(bingo_board_state, spots, picked_number):
    for board_num in range(len(bingo_board_state)):
        for row in range(len(bingo_board_state[0])):
            for element in range(len(bingo_board_state[0][0])):
                if bingo_board_state[board_num][row][element] == picked_number:
                    spots[board_num][row][element] = 1


def check_rows(spots):
    found = False
    for board_num in range(len(spots)):
        for row in range(len(spots[0])):
            if spots[board_num][row][0] == 1 and spots[board_num][row][1] == 1 and spots[board_num][row][2] == 1 and spots[board_num][row][3] == 1 and spots[board_num][row][4] == 1:
                return board_num, row, True


def check_cols(spots):
    for board_num in spots:
        for board_col in spots[board_num]:
            for board_element in spots[board_num][board_col]:
                if spots[board_num][board_element][board_col] != 1:
                    continue
                return board_num


data = open("inputs.txt")

numbers = list(map(int, data.readline().split(',')))
boards = list()
bingo_spots = list()

for i in data:
    boards.append(np.array([list(map(int, data.readline().split())),
                            list(map(int, data.readline().split())),
                            list(map(int, data.readline().split())),
                            list(map(int, data.readline().split())),
                            list(map(int, data.readline().split()))
                            ]))

    bingo_spots.append(np.zeros((5, 5)))

count = 0
print(numbers)

for i in range(len(boards)):
    print()
winner = [0, 0, False]
for i in numbers:
    print("Looking for {0}".format(i))
    if count > 4:
        # check_cols(spots=bingo_spots)
        winner = check_rows(bingo_spots)
    if len(winner) != 0 and winner[2]:
        break
    check_number(boards, bingo_spots, i)
    count = count + 1

print(winner)
print(bingo_spots)
