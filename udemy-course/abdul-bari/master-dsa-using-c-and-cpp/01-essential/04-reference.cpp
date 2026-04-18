#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int a = 10;
    int &r =a; // reference needed to initialized otherwise it show error
    cout << a << endl << r << endl;
    a = 12;
    cout << a << endl << r << endl;
    int b =11;
    r = b;  // this will not change the reference instead change the value at that address
    cout << a << endl << r << endl;
    cout << b << endl;
    return 0;
}
