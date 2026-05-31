#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int func(int n) {
    if (n>100) {
        return n - 10;
    } else {
        return func(func(n+11));
    }
}

int main() {
    cout << func(95);
    return 0;
}
