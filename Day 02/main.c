#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    char const* const fileName = argv[1];
    FILE* file = fopen(fileName, "r");
    char line[20];

    // part a
    int depth = 0;
    int horizontalPos = 0;

    while (fgets(line, sizeof(line), file)) {
        int num = line[strlen(line) - 2] - '0';

        line[strlen(line) - 1] = '\0';
        line[strlen(line) - 1] = '\0';
        line[strlen(line) - 1] = '\0';

        if(strcmp(line, "forward") == 0) {
            horizontalPos += num;
        } else if(strcmp(line, "down")) {
            depth -= num;
        } else if(strcmp(line, "up")) {
            depth += num;
        }
    }

    printf("hori: %i\ndepth: %i\na: %i\n", horizontalPos, depth, horizontalPos * depth);


    fclose(file);

    // part b
    FILE* file1 = fopen(fileName, "r");

    int aim = 0;
    depth = 0;
    horizontalPos = 0;

    while (fgets(line, sizeof(line), file1)) {
        int num = line[strlen(line) - 2] - '0';

        line[strlen(line) - 1] = '\0';
        line[strlen(line) - 1] = '\0';
        line[strlen(line) - 1] = '\0';

        if(strcmp(line, "forward") == 0) {
            horizontalPos += num;
            depth += aim * num;
        } else if(strcmp(line, "down")) {
            aim -= num;
        } else if(strcmp(line, "up")) {
            aim += num;
        }
    }

    printf("hori: %i\ndepth: %i\na: %i\n", horizontalPos, depth, horizontalPos * depth);

    fclose(file);

    return 0;
}
