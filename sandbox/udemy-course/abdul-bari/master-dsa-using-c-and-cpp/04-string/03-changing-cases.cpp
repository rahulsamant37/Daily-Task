#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    string str = "RaHul";
    int n = str.size();
    char cur;
    for (int i = 0; i < n; i++) {
        if(str[i]<97) {
            cur = str[i] + 32;
            cout << cur << " ";
        } else {
            cur = str[i] - 32;
            cout << cur << " ";
        }
    }
    return 0;
}
