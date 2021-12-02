file = open("inputs.txt")

data = file.readlines()

size = len(data[0]) - 1
ones = [0] * size
zeros = [0] * size

gamma = ['0'] * size
epsilon = ['0'] * size

for i in data:
    for j in range(len(i)):

        if i[j] == '0':
            zeros[j] = zeros[j] + 1

        elif i[j] == '1':
            ones[j] = ones[j] + 1

for i in range(len(ones)):

    if ones[i] < zeros[i]:
        gamma[i] = '0'
        epsilon[i] = '1'

    else:
        gamma[i] = '1'
        epsilon[i] = '0'

gamma = ''.join(gamma)
epsilon = ''.join(epsilon)

print(int(gamma, 2) * int(epsilon, 2))
