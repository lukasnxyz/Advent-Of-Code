#include <stdio.h>

#define LINESIZE 13
#define LOOPSIZE 12

int btoi(int length, int arr[]) {
    int output=0;

    for(int i = 0; i < length; i++) {
        output *= 2;
        output += arr[i];
    }

    return output;
}

int main(int argc, char *argv[]) {
    // part a
    char const* const fileName = argv[1];
    FILE *file = fopen(fileName, "r");
    char line[LINESIZE];

    int gamma[LINESIZE];
    int epsilon[LINESIZE];
    int zero = 0;
    int one = 0;
    int arrPos = 0;

    for(int i = 0; i < LOOPSIZE; i++) {
        while(fgets(line, sizeof(line), file)) {
            if(line[i] == '0') {
                zero++;
            } else if(line[i] == '1') {
                one++;
            }
        }

        if(zero > one) {
            gamma[arrPos] = 0;
            epsilon[arrPos] = 1;
            arrPos++;
        } else if(zero < one) {
            gamma[arrPos] = 1;
            epsilon[arrPos] = 0;
            arrPos++;
        }

        zero = 0;
        one = 0;
        rewind(file);
    }

    printf("%i\n", btoi(LOOPSIZE, gamma) * btoi(LOOPSIZE, epsilon));

    fclose(file);

    return 0;
}
