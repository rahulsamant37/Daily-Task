#include <bits/stdc++.h>
using namespace std;
#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int n, m;
    cin >> n >> m;
    n ^= m;
    m ^= n;
    n ^= m;
    cout << n << ' ' << m << endl;
    return 0;
}
