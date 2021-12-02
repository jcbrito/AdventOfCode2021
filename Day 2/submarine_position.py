depth = 0
horizontal = 0

file = open("inputs.txt")

for x in file:
    cmd = x.split(" ")


    if cmd[0] == "forward":
        horizontal += int(cmd[1])

    elif cmd[0] == "up":
        depth -= int(cmd[1])

    else:
        depth += int(cmd[1])

print(int(depth) * int(horizontal))
