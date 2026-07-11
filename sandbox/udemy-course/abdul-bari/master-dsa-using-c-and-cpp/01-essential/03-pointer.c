#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int a = 10;
    int *p;
    p = &a;
    int *q;
    q = (int *)malloc(5 * sizeof(int));
    printf("%d", *q);
    printf("%d", *p);
    free(q);
    return 0;
}
