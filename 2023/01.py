import re

def charToInt(letter):
    return ord(letter) - ord('A') + 1

def p1():
    sum_calibration_values = 0

    with open("input.txt", "r") as input:
        for line in input:
            line_nums = []
            for letter in line:
                if letter.isdigit():
                    line_nums.append(letter)

            line_ints = str(line_nums[0]) + (str(line_nums[len(line_nums) - 1]))
            sum_calibration_values += int(line_ints)

    return sum_calibration_values

# Not my code!
# -- start
def f(line):
    for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        line = line.replace(n, n + str(i+1) + n)
    x = re.findall(r'(\d)', line)
    return int(x[0] + x[-1])
# -- end

def p2():
    sum_calibration_values = 0

    nums_dict = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "zero": 0
    }

    with open("input.txt", "r") as input:
        for line in input:
            line_dict = {}
            for name, num in nums_dict.items():
                if name in line:
                    line_dict[name] = line.find(name)

                if str(num) in line:
                    line_dict[str(num)] = line.find(str(num)) # error here, if there are two of the saem number, it doesn't add

            smallest_pos = 100
            smallest_num = "0"

            largest_pos = 0
            largest_num = "0"

            for name, pos in line_dict.items():
                if pos < smallest_pos:
                    smallest_num = name
                    smallest_pos = pos

            for name, pos in line_dict.items():
                if pos > largest_pos:
                    largest_num = name
                    largest_pos = pos

            if not largest_num.isdigit():
                largest_num = str(nums_dict[largest_num])

            if not smallest_num.isdigit():
                smallest_num = str(nums_dict[smallest_num])

            line_n = smallest_num + (largest_num)

            sum_calibration_values += int(line_n)

    return sum_calibration_values

def main():
    print("p1: " + str(p1()))
    print("p2: " + str(p2()))

    print("Not mine p2: " + " " + str(sum(map(f, open('input.txt'))))) # Not my code!

if __name__ == "__main__":
    main()
