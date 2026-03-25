#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int n;
    cin >> n;
    string str="";
    while(n>0) {
        int re = n%2;
        // 0 + 48 = 48  → '0'
        // 1 + 48 = 49  → '1'
        // 1 + 48 = 49  → '1'
        str.push_back(re+'0');
        n/=2;
    }
    reverse(str.begin(), str.end());
    for (char i: str) {
        cout << i;
    }
    cout << endl;
    return 0;
}