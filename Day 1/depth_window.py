f = open("input.txt", "r")
lines = f.readlines()
count = 0

for i in range(len(lines)):
    if i == len(lines) - 3:
        break
    prev = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    curr = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    if prev < curr:
        count += 1

print(count)
