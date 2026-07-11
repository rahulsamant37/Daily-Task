#include <stdio.h>

int main(void) {
    int a[5];
    int b[5] = {2, 3, 4, 5, 6};
    for (int i = 0; i < 5; i++) {
        printf("%d\n",b[i]);
    }
    printf("%zu", sizeof(a));
    return 0;
}
