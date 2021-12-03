file = open("inputs.txt")
file2 = open("inputs.txt")

data = file.readlines()
data2 = file2.readlines()

print(data)
print(data2)

size = len(data[0]) - 1


def get_freq(data_set):
    tmp_ones = [0] * size
    tmp_zeros = [0] * size


    for x in data_set:
        for n in range(len(x)):

            if x[n] == '0':
                tmp_zeros[n] = tmp_zeros[n] + 1

            elif x[n] == '1':
                tmp_ones[n] = tmp_ones[n] + 1

    print(tmp_ones)
    print(tmp_zeros)

    return tmp_zeros, tmp_ones


for i in range(size):

    ones, zeros = get_freq(data)

    if len(data) == 1:
        break

    bit = '1'

    if ones[i] < zeros[i]:
        bit = '0'

    for j in data:

        if len(data) == 1:
            break

        if j[i] != bit:
            data.remove(j)

print(data)
"""for i in range(size):

    ones, zeros = get_freq(data2)

    if len(data2) == 1:
        break

    bit = '0'

    if ones[i] > zeros[i]:
        bit = '1'

    for j in data2:

        if len(data2) == 1:
            break

        if j[i] != bit:
            data2.remove(j)

print(data2)"""

