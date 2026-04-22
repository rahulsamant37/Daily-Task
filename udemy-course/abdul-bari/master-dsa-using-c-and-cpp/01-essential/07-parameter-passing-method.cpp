#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int add(int a, int b) {
    int c = a + b;
    return c;
}

// Passing by value
int add_one(int a) {
    a++;
    return 0;
}

// passing by reference in c
void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

// passing by reference in c++
void swapcpp(int &a, int &b) {
    int temp;
    temp = a;
    a = b;
    b = temp;
}

int main() {
    int a = 10, b = 20;
    cout << add(a, b) << endl;

    add_one(a);
    cout << a << endl;

    swap(&a, &b);
    cout << a << " " << b << endl;

    swapcpp(a, b);
    cout << a << " " << b << endl;

    return 0;
}
