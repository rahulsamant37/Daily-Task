#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

// array are always pass by reference can't pass it by value
void func(int arr[ ]) {
    cout << sizeof(arr)/sizeof(int) << endl;
}

void func2(int arr[ ], int n) {
    cout << "func2 start from here" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << endl;
    }
}

// this will also work the same as above
void func3(int *arr, int n) {
    cout << "func3 start from here" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << endl;
    }
}

// array as pointer
int * fun(int size) {
    int *p;
    p = new int[size];
    for (int i = 0; i < size; i++) {
        p[i] = i+1;
    }
    return  p;
}

int main() {
    int arr[ ] = {2, 3, 4, 5, 6};
    int n = size(arr);
    for (int i: arr) {
        cout << i << " ";
    }
    cout << endl;
    func(arr);
    cout << sizeof(arr)/sizeof(int) << endl;
    func2(arr, n);
    func3(arr, n);
    int *p = fun(5);
    // is you create a pointer at heap you can access the pointer anywhere
    cout << "this is where fun start" << endl;
    for (int i = 0; i < 5; i++) {
        cout << p[i] << endl;
    }
    return 0;
}
