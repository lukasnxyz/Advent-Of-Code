#include <stdio.h>
#include "input.h"

int main(int argc, char argv[]) {
    // part a
    int increase = 0;
    int decrease = 0;

    for(int i = 0; i < LENGTH; i++) {
        if(nums[i+1] > nums[i]) {
            increase++;
        } else {
            decrease++;
        }
    }

    printf("%i\n", increase);

    // part b
    increase = 0;

    for(int i = 0; i < LENGTH; i += 1) {
        int a = nums[i] + nums[i+1] + nums[i+2];
        int b = nums[i+1] + nums[i+2] + nums[i+3];

        if(i+3 > 2000) {
            i = 10;
            break;
        }

        if(b > a) {
            increase++;
        } else {
            continue;
        }
    }

    printf("%i\n", increase);

    return 0;
}
