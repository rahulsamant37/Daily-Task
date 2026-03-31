/*
Author: Baldy Cape
Created: 2026-02-27 00:18:46
*/

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    
    cout << "\n=== Pointer Arithmetic ===\n";
    int arr[] = {10, 20, 30, 40, 50};
    int *q = arr;  // points to arr[0]
    for (int i = 0; i < 5; i++) {
        cout << "q+" << i << " -> address: " << (q+i)
             << "  value: " << *(q+i) << "\n";
    }
    
    return 0;
}