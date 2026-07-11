#include <bits/stdc++.h>
#include <memory>
using namespace std;

#define endl '\n'

int main() {
    auto ptr = make_unique<int[]>(5);
    cout << ptr[0];
    cout << endl;
    cout << *(&ptr[0]+4);
    return 0;
}
