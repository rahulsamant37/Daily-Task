#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int power(int m, int n) {
    if (n == 0) {
        return 1;
    } else {
        return power(m, n-1) * m;
    }

}

int power_optimized(int m, int n) {
    if (n == 0) {
        return 1;
    } else if (n%2==0) {
        return power_optimized(m*m, n/2);
    } else {
        return m * power_optimized(m*m, (n - 1) / 2);
    }
}

int main() {
    cout << power(10, 2) << endl;
    cout << power_optimized(10, 2);
    return 0;
}
