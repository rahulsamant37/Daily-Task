#include <bits/stdc++.h>
using namespace std;

#define endl '\n'


void func(int n) {
    if (n>0) {
        cout << n << " ";
        func(n-1);
        /* 
         * Tail recursion is a type of recursion where the recursive call is the 
         * last operation performed in the function, allowing optimization into 
         * iteration by some compilers/interpreters.
        */
    }
}

int main() {
    int n = 10;
    func(n);
    return 0;
}
