#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void printNumbers(int n) {
    if (n==0) {
        return;
    }
    printNumbers(n - 1);  // Recursive call first
    cout << n << " ";     // Processing after recursion
}

int main() {
    printNumbers(5);
    return 0;
}
