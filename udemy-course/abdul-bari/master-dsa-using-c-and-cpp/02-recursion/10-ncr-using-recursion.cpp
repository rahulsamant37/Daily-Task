#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int ncr(int n, int r) {
    if(r==0 || n == r) {
        return 1;
    } else {
        return ncr(n-1, r-1) + ncr(n-1, r);
    }
}

int main() {
    cout << ncr(4,2);
    return 0;
}
