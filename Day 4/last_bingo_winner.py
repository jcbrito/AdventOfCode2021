import numpy as np


def check_number(bingo_board_state, spots, picked_number):
    for board_num in range(len(bingo_board_state)):
        for row in range(len(bingo_board_state[0])):
            for element in range(len(bingo_board_state[0][0])):
                if bingo_board_state[board_num][row][element] == picked_number:
                    spots[board_num][row][element] = 1


def check_rows(spots):
    for board_num in range(len(spots)):
        for row in range(len(spots[0])):
            if spots[board_num][row][0] == 1 and spots[board_num][row][1] == 1 and spots[board_num][row][2] == 1 and \
                    spots[board_num][row][3] == 1 and spots[board_num][row][4] == 1:
                return board_num, row, True
    return 0, 0, False


def check_cols(spots):
    for board_num in range(len(spots)):
        for col in range(len(spots[0])):
            if spots[board_num][0][col] == 1 and spots[board_num][1][col] == 1 and spots[board_num][2][col] == 1 and \
                    spots[board_num][3][col] == 1 and spots[board_num][4][col] == 1:
                return board_num, col, True
    return 0, 0, False


def sum_unmarked(bingo_board, marked):
    total_marked = sum(sum(bingo_board))

    for row in range(len(marked)):
        for element in range(len(marked[row])):
            if marked[row][element] == 1:
                total_marked = total_marked - bingo_board[row][element]

    return total_marked


data = open("inputs.txt")

numbers = list(map(int, data.readline().split(',')))
boards = list()
bingo_spots = list()
last_winner = list()
last_winner_spots = list()

for i in data:
    boards.append(np.array([list(map(int, data.readline().split())),
                            list(map(int, data.readline().split())),
                            list(map(int, data.readline().split())),
                            list(map(int, data.readline().split())),
                            list(map(int, data.readline().split()))
                            ]))

    bingo_spots.append(np.zeros((5, 5)))

count = 0
last_called_index = 0
print(sorted(numbers))

print(len(boards))
for i in numbers:
    if len(boards) == 0:
        break

    check_number(boards, bingo_spots, i)
    print("Looking for {0}".format(i))

    if count > 4:
        winner_rows = check_rows(bingo_spots)
        winner_cols = check_cols(bingo_spots)


    while True:
        winner_rows = check_rows(bingo_spots)
        if not winner_rows[2]:
            break
        print("Board {0} has won".format(winner_rows[0]))
        last_winner.append(boards.pop(winner_rows[0]))
        last_winner_spots.append(bingo_spots.pop(winner_rows[0]))

    while True:
        winner_cols = check_cols(bingo_spots)
        if not winner_cols[2]:
            break
        print("Board {0}".format(winner_cols[0]))
        last_winner.append(boards.pop(winner_cols[0]))
        last_winner_spots.append(bingo_spots.pop(winner_cols[0]))

    count = count + 1

total = 0
for val in last_winner[0]:
    total = total + val
print(sum_unmarked(last_winner[-1], last_winner_spots[-1]) * numbers[count-1])
