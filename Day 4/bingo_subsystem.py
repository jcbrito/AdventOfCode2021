import numpy as np


def check_number(bingo_board_state, spots, picked_number):
    for board_num in range(len(bingo_board_state)):
        for row in range(board_num):
            for element in range(row):
                if bingo_board_state[board_num][row][element] == picked_number:
                    spots[board_num][row][element] = 1


def check_rows(spots):
    for board_num in spots:
        for board_row in spots[board_num]:
            for board_element in spots[board_num][board_row]:
                if spots[board_num][board_row][board_element] != 1:
                    continue
                return board_num


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

for i in numbers:
    # if count > 4:
    # check_cols(spots=bingo_spots)
    # check_rows(spots=bingo_spots)
    check_number(boards, bingo_spots, i)
    count = count + 1

print(boards)
print(bingo_spots)
