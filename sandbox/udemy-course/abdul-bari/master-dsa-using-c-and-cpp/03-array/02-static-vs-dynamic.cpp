#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    // in c we have to declare the size of array at compile time
    // whereas in c++ we can declare it in run time
    int arr[5];
    int n;
    cin >> n;
    int arr2[n];
    cout << arr2[0] << endl;

    // to access heap and create an array
    int *ptr;
    ptr = new int[5];
    arr[0] = 10;
    cout << arr[0] << endl;
    ptr[0] = 10;
    cout << ptr[0] << endl;
    delete []ptr;
    return 0;
}
