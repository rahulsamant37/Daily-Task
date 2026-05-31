#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

vector<int> memo;

int fibonaccinum(int n) {
    if (n<=1) {
        return n;
    } else {
        return fibonaccinum(n-1) + fibonaccinum(n-2);
    }
}

int fibonaccimemo(int n) {
    if (memo.size() < static_cast<size_t>(n + 1)) {
        memo.assign(n + 1, -1);
    }
    if (n<=1) {
        return n;
    }
    if (memo[n]!=-1) {
        return memo[n];
    }
    
    memo[n] = fibonaccimemo(n-1) + fibonaccimemo(n-2);
    return memo[n];
}

int main() {
    cout << fibonaccinum(7) << endl;
    cout << fibonaccimemo(7);
    return 0;
}
