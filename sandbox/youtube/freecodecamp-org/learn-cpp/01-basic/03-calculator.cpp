#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

long long calculator(int a, int b, char ops) {
    if (ops == '+') {
        return a+b;
    } else if (ops == '-') {
        return a-b;
    } else if (ops == '*') {
        long long mul = a*b;
        return mul;
    } else if (ops == '/') {
        if (b!=0) {
            return a/b;
        } else {
            cout << "denominator can't be ";
            return 0;
        }
    }
}

int main() {
    int n, m;
    char ops;
    cin >> n >> ops >> m;
    cout << calculator(n, m, ops);
    return 0;
}
