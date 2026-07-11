#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int *p, *q;
    p = new int[5];
    p[0] = 101, p[1] = 10, p[2] = 3, p[3] = 12, p[4] = 20;
    q = new int[10];
    for (int i = 0; i < 5; i++) {
        q[i] = p[i];
        cout << q[i] << " ";
    }
    delete []p;
    p = q;
    q = NULL;
    cout << endl;
    for (int i = 0; i < 10; i++) {
        cout << p[i] << " ";
    }
    delete []p;
    return 0;
}
