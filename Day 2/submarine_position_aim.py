depth = 0
horizontal = 0
aim = 0

file = open("inputs.txt")

for x in file:
    cmd = x.split(" ")
    print(cmd)
    if cmd[0] == "forward":
        horizontal += int(cmd[1])
        depth += int(cmd[1]) * aim

    elif cmd[0] == "up" :
        aim -= int(cmd[1])

    else:
        aim += int(cmd[1])

print(int(depth) * int(horizontal))