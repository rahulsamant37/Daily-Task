/*
Author: Baldy Cape
Created: 2026-02-26 22:31:22
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n = 10;
    int *p = &n;

    cout << "=== Basic Pointer ===\n";
    cout << "Value of n       : " << n   << "\n"; // 10
    cout << "Address of n     : " << &n  << "\n"; // e.g. 0x61ff08
    cout << "p holds address  : " << p   << "\n"; // same as &n
    cout << "Address of p     : " << &p  << "\n"; // p itself lives somewhere
    cout << "Dereferenced *p  : " << *p  << "\n"; // 10

    cout << "\n=== Modifying via Pointer ===\n";
    *p = 99;  // change n through the pointer
    cout << "After *p = 99, n = " << n << "\n"; // 99

    return 0;
}