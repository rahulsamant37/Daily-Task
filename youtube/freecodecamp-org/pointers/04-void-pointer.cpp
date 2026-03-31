/*
Author: Baldy Cape
Created: 2026-02-27 00:20:42
*/

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    
    int    i = 42;
    float  f = 3.14f;
    char   c = 'Z';

    void *vp;   // can point to ANY type, but cannot be dereferenced directly

    cout << "=== void* pointing to int ===\n";
    vp = &i;
    cout << "Address stored in vp : " << vp << "\n";
    cout << "Value (cast needed)  : " << *(int*)vp << "\n";

    cout << "\n=== void* pointing to float ===\n";
    vp = &f;
    cout << "Address stored in vp : " << vp << "\n";
    cout << "Value (cast needed)  : " << *(float*)vp << "\n";

    cout << "\n=== void* pointing to char ===\n";
    vp = &c;
    cout << "Address stored in vp : " << vp << "\n";
    cout << "Value (cast needed)  : " << *(char*)vp << "\n";

    cout << "\n=== Modifying through void* ===\n";
    vp = &i;
    *(int*)vp = 100;   // cast first, then dereference
    cout << "i after modifying via vp : " << i << "\n";

    cout << "\n=== Generic swap using void* ===\n";
    // manually swap two ints using void*
    int a = 5, b = 9;
    void *va = &a, *vb = &b;
    int temp = *(int*)va;
    *(int*)va = *(int*)vb;
    *(int*)vb = temp;
    cout << "After swap: a = " << a << ", b = " << b << "\n";
    
    return 0;
}