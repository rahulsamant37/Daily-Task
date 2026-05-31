#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int factorial(int n) {
    if (n==0) {
        return 1;
    }
    else {
        return n*factorial(n - 1);
    }
}

int main() {
    cout << factorial(5);
    return 0;
}
