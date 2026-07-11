#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int a = 10;
    int &r =a; // reference needed to initialized otherwise it show error
    cout << "a = " << a << endl << "r = " << r << endl;
    cout << endl;
    cout << "========== after a = 12 ============" << endl;
    cout << endl;
    a = 12;
    cout << "a = " << a << endl << "r = " << r << endl;
    cout << endl;
    cout << "========== after r = b = 11 ============" << endl;
    cout << endl;
    int b =11;
    r = b;  // this will not change the reference instead change the value at that address
    cout << "a = " << a << endl << "r = " << r << endl;
    cout << "b = " << b << endl;
    return 0;
}
