#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int n;
    cin >> n;
    int sum = 0;
    int cnt = 0;
    while(n>0) {
        int rem = n%10;
        sum+=(rem*(1<<cnt));
        cnt++;
        n/=10;
    }
    cout << sum;
    cout << endl;
    
    return 0;
}