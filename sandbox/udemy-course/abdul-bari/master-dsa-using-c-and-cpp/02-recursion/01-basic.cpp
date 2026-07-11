#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void func1(int a) {
    if (a > 0) {
        cout << a << " ";
        func1(a-1);
    }
}

void func2(int a) {
    if (a > 0) {
        func2(a-1);
        cout << a << " ";
    }
}

int main() {
    int n = 10;
    // cin >> n;
    func1(n);
    cout << endl;
    func2(n);

    return 0;
}
