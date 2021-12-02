f = open("input.txt")
x = 0
prev = int(f.readline())
count = 0;
for i in f:
    next = int(i)
    if next > prev : count += 1
    prev = next;

print(count)
