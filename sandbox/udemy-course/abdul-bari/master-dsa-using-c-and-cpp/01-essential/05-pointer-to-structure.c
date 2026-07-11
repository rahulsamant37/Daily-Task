#include <stdio.h>
#include <stdlib.h>

struct rectangle {
    int length;
    int breadth;
};
int main(void) {
    struct rectangle *ptr;
    ptr = (struct rectangle *)malloc(sizeof(struct rectangle));
    ptr->length = 15;
    ptr->breadth = 10;
    printf("%d %d",ptr->length, ptr->breadth);
    free(ptr);
    return 0;
}
