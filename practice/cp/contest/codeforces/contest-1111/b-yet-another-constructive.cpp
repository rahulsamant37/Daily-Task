/*
Author: Rahul Samant
Created: 2026-07-18 20:43:00
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> pii;

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define sz(x) (int)(x).size()
#define rep(i, a, b) for(int i = (a); i < (b); ++i)
#define endl '\n'

#ifdef LOCAL
#define debug(x) cerr << "[DEBUG] " << #x << " = " << (x) << endl
#else
#define debug(x)
#endif

const int MOD = 1e9 + 7;
const ll INF = 1e18;

void setup_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
}

void solve() {
    int n, k, m;
    cin >> n >> k >> m;
    
    if (k > m) {
        cout << "NO" << endl;
        return;
    }
    
    cout << "YES" << endl;
    rep(i, 0, n) {
        if ((i + 1) % k == 0) {
            cout << m - k + 1 << (i == n - 1 ? "" : " ");
        } else {
            cout << 1 << (i == n - 1 ? "" : " ");
        }
    }
    cout << endl;
}

int main() {
    setup_io();
    int t;
    cin >> t;
    while(t--) {
        solve();
    }
    return 0;
}
