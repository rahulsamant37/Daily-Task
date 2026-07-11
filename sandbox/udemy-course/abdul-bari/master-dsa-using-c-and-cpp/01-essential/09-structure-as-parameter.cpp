#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

struct rectangle {
    int length;
    int breadth;
};

int area(struct rectangle r) {
    return r.breadth*r.length;
}

// but if we pass &r it will pass by reference and change the real value also
void changeLength(struct rectangle &r) {
    r.length++;
}

void changeLengthP(struct rectangle *r, int length) {
    r->length = length;
}

struct test {
    int arr[5];
    int n;
};

void fun(struct test t) {
    t.arr[0] = 10;
    t.arr[1] = 20;
    t.arr[2] = 30;
    t.arr[3] = 40;
    t.arr[4] = 50;
}

int main() {
    struct rectangle rec = {2, 10};
    cout << area(rec) << endl;
    cout << rec.length << endl;
    changeLength(rec);
    cout << rec.length << endl;
    changeLengthP(&rec, 2);
    cout << rec.length << endl;

    cout << "normally you can't pass array by value but with struct you can" << endl;
    struct test t = {{1, 2, 3, 4, 5}, 5};
    fun(t);
    for (int i: t.arr) {
        cout << i << endl;
    }
    return 0;
}
