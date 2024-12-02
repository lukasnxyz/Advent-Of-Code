#with open("02.txt", "r") as file:
#    data = [[int(num) for num in line.split(" ")] for line in file]

##data = [[7, 6, 4, 2, 1], 
##        [1, 2, 7, 8, 9],
##        [9, 7, 6, 2, 1],
##        [1, 3, 2, 4, 5],
##        [8, 6, 4, 4, 1],
##        [1, 3, 6, 7, 9]]
#
#def is_safe(line):
#    less_than = line[0] < line[1]
#
#    for i in range(len(line)-1):
#        match less_than:
#            case True:
#                if line[i] >= line[i+1] or abs(line[i+1]-line[i]) > 3:
#                    return False, i
#            case False:
#                if line[i] <= abs(line[i+1] or line[i]-line[i+1]) > 3:
#                    return False, i+1
#    return True, -1
#
#unsafe = 0
#for line in data:
#    safe, ind = is_safe(line)
#    if not safe:
#        modified_line = line[:ind] + line[ind+1:]
#        safe, _ = is_safe(modified_line)
#        if not safe:
#            unsafe += 1
#
#print("safe:", len(data)-unsafe)

def read_input():
    with open("02.txt", "r") as f:
        return f.read().strip().split("\n")

def part1(data):
    count = 0
    for i in range(len(data)):
        data[i] = list(map(int, data[i].split(" ")))
    for i in data:
        if check(i):
            count += 1
    return count


def part2(data):
    count = 0
    for i in data:
        if solve(i):
            count += 1
    return count


def solve(data):
    if check(data):
        return True
    for i in range(len(data)):
        md = data[:i] + data[i + 1 :]
        if check(md):
            return True
    return False


def check(data):
    count = 0
    for i in range(len(data) - 1):
        if data[i] > data[i + 1] and abs(data[i] - data[i + 1]) < 4:
            count += 1
    if (len(data) - 1) == count:
        return True
    count = 0
    for i in range(len(data) - 1):
        if data[i] < data[i + 1] and abs(data[i] - data[i + 1]) < 4:
            count += 1
    if (len(data) - 1) == count:
        return True

    return False


data = read_input()
print(part1(data))
print(part2(data))
