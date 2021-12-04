file = open("inputs.txt")
file2 = open("inputs.txt")

data = file.readlines()
data2 = file2.readlines()

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

    return tmp_zeros, tmp_ones


for i in range(size):

    zeros, ones = get_freq(data)

    bit = '1'

    if ones[i] < zeros[i]:
        bit = '0'

    tmp = data[-1]
    data = [x for x in data if x[i] == bit]

    if len(data) == 0:
        data = tmp
        break


oxygen = int(''.join(data), 2)

for i in range(size):

    zeros, ones = get_freq(data2)

    bit = '0'

    if ones[i] < zeros[i]:
        bit = '1'

    tmp = data2[-1]
    data2 = [x for x in data2 if x[i] == bit]

    if len(data2) == 0:
        data2 = tmp
        break

co2 = int(''.join(data2), 2)

print(oxygen * co2)

