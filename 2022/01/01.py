def sum_cals(cals):
    total_cals = 0

    for item in cals:
        total_cals += int(item)

    return total_cals

def max_cals_elf():
    max_cals = 0

    with open("input.txt", "r") as input:
        inputs_single_elf = []

        for line in input:
            if line == '\n':
                cals = sum_cals(inputs_single_elf)

                if max_cals < cals:
                    max_cals = cals

                inputs_single_elf = []

                continue

            inputs_single_elf.append(line)

    return max_cals

def max_cals_elf_three():
    max_cals_three = [0, 0, 0]

    with open("input.txt", "r") as input:
        inputs_single_elf = []

        for line in input:
            if line == '\n':
                cals = sum_cals(inputs_single_elf)

                for index, elf in enumerate(max_cals_three):
                    if max_cals_three[index] < cals:
                        if index == 0:
                            max_cals_three[index + 2] = max_cals_three[index + 1]
                            max_cals_three[index + 1] = max_cals_three[index]
                        elif index == 1:
                            max_cals_three[index] = max_cals_three[index + 1]

                        max_cals_three[index] = cals

                        break

                inputs_single_elf = []

                continue

            inputs_single_elf.append(line)

    print(max_cals_three)

    return sum_cals(max_cals_three)

def main():
    highest_cal_elf = max_cals_elf()
    top_three_combined = max_cals_elf_three()

    print(highest_cal_elf)
    print(top_three_combined)

if __name__ == "__main__":
    main()
