#include <stdio.h>


#define endl '\n'

struct rectangle {
    int length;
    int breadth;
};

int area(struct rectangle r) {
    return r.breadth*r.length;
}

int main() {
    struct rectangle rec = {2, 10};
    printf("%d", area(rec));
    return 0;
}
