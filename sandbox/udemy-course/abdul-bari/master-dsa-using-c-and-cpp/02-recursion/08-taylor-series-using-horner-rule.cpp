#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

double e(int x, int n) {

    static double s = 1;
    if (n==0) {
        return s;
    }
    s = 1 + x*s/n;
    return e(x, n-1);
}

double e_iterative(int x, int n) {
    double r = 1;
    for (int i = n; i > 0; i--) {
        r = 1 + r*x/i;
    }
    return r;
}

int main() {
    cout << e(1, 10);
    return 0;
}
