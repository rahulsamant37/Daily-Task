#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    // different ways to delecare an array
    int arr1[5];
    int arr2[5] = {1,23,4,5};
    int arr3[] = {1,2,4,4};
    int arr4[5] = {0};

    cout << "------# arr1 # -------" << endl;
    for (int i:arr1) {
        cout << i << endl;
    }
    cout << "------# arr2 # -------" << endl;
    for (int i: arr2) {
        cout << i << endl;
    }
    cout << "------# arr3 # -------" << endl;
    for (int i: arr3) {
        cout << i << endl;
    }
    cout << "------# arr4 # -------" << endl;
    for (int i: arr4) {
        cout << i << endl;
    }
    return 0;
}
