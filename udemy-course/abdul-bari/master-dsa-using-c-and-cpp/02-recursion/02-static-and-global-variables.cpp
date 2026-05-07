#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int func(int n) {
    static int x = 0;
    if (n>0) {
        x++;
        return func(n-1) + x;
    }
    return 0;
}

int func2(int n) {
    int x = 0;
    if (n>0) {
        x++;
        return func2(n-1) + x;
    }
    return 0;
}

int func3(int n) {
    if (n>0) {
        return func3(n-1) + n;
    }
    return 0;
}

int main() {
    int n = 5;
    cout << func(n) << endl;  // 25
    cout << func2(n) << endl; // 5
    cout << func3(n) << endl; // 15
    return 0;
}
