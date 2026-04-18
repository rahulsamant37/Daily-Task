#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

struct rectangle {
    int length;
    int breadth;
};

int main() {
    struct rectangle r = {10, 5};
    struct rectangle *ptr = &r;
    r.breadth = 10;
    ptr->length = 20; // can also use (*ptr).length
    cout << r.length << " " << r.breadth << endl;
    struct rectangle *p;
    p = new rectangle;
    p->breadth = 10;
    p->length = 15;
    cout << p->breadth << " " << p->length;
    delete p;

    return 0;
}
