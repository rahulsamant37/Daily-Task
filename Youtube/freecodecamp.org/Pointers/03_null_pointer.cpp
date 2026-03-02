/*
Author: Baldy Cape
Created: 2026-02-27 00:19:20
*/

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    
    cout << "\n=== Null Pointer ===\n";
    int *null_p = nullptr;
    cout << "null_p = " << null_p << "\n"; // 0
    // *null_p = 5; // !! never dereference a null pointer — crash
    
    return 0;
}