#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void tower_of_hanoi(int n, int a, int b, int c) {
    if (n>0) {
        tower_of_hanoi(n-1, a, c, b);
        cout << "move from " << a << " to " << c << endl;
        tower_of_hanoi(n-1, b, a, c);
    }
}

int main() {
    tower_of_hanoi(3, 1, 2, 3);
    return 0;
}
