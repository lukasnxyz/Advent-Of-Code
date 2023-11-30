import time
def p1():
    score = 0
    with open("input.txt", "r") as input:
        for line in input:
            input_line = []

            for char in line:
                if char == " ":
                    continue
                input_line.append(char)

            # Y is Paper
            # X is Rock
            # Z is Scissors

            # A is Rock
            # B is Paper
            # C is Scissors
            if input_line[1] == "Y":
                score += 2
            elif input_line[1] == "X":
                score += 1
            elif input_line[1] == "Z":
                score += 3

            if input_line[0] == "A":
                if input_line[1] == "Y":
                    score += 6
                elif input_line[1] == "X":
                    score += 3
                elif input_line[1] == "Z":
                    score += 0
            elif input_line[0] == "B":
                if input_line[1] == "Y":
                    score += 3
                elif input_line[1] == "X":
                    score += 0
                elif input_line[1] == "Z":
                    score += 6
            elif input_line[0] == "C":
                if input_line[1] == "Y":
                    score += 0
                elif input_line[1] == "X":
                    score += 6
                elif input_line[1] == "Z":
                    score += 3

    return score

def p2():
    score = 0

    with open("input.txt", "r") as input:
        for line in input:
            input_line = []

            for char in line:
                if char == " ":
                    continue

                input_line.append(char)

            # Y is Paper 2
            # X is Rock 1
            # Z is Scissors 3

            # A is Rock
            # B is Paper
            # C is Scissors

            # draw
            if input_line[1] == "Y":
                score += 3

                if input_line[0] == "A":
                    score += 1 # X
                elif input_line[0] == "B":
                    score += 2 # Y
                elif input_line[0] == "C":
                    score += 3 # Z
            # lose
            elif input_line[1] == "X":
                if input_line[0] == "A":
                    score += 3 # Z
                elif input_line[0] == "B":
                    score += 1 # X
                elif input_line[0] == "C":
                    score += 2 # y
            # win
            elif input_line[1] == "Z":
                score += 6

                if input_line[0] == "A":
                    score += 2 # Y
                elif input_line[0] == "B":
                    score += 3 # Z
                elif input_line[0] == "C":
                    score += 1 # X

    return score

def main():
    print(p1())
    print(p2())

if __name__ == "__main__":
    main()
