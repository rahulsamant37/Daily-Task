#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int sum_n_natural_number(int n) {
    if (n == 0) {
        return 0;
    } else {
        return sum_n_natural_number(n-1) + n;
    }
}

int main() {
    cout << sum_n_natural_number(10);
    return 0;
}
