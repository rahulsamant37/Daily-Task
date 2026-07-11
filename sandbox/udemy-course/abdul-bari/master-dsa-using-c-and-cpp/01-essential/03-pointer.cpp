#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

struct rectangle {
    int length;
    int breadth;
};

int main() {
    int a = 10;
    int *p;
    p = &a;
    int *q;
    q = new int[5];
    cout << *q;
    cout << *p;
    delete [ ] q; // to delete heap space it needed manually


    cout << endl;
    // pointer always take 8 bits
    int *p1;
    char *p2;
    float *p3;
    double *p4;
    struct rectangle *p5;

    cout << sizeof(p1) << endl << sizeof(p2) << endl << sizeof(p3) << endl << sizeof(p4) << endl  << sizeof(*p5);
    return 0;
}
