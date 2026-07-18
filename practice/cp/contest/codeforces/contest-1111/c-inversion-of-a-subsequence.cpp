/*
Author: Rahul Samant
Created: 2026-07-18 20:59:25
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
    int n;
    cin >> n;
    vi a(n), b(n);
    rep(i, 0, n) cin >> a[i];
    rep(i, 0, n) cin >> b[i];
    
    vi d;
    rep(i, 0, n) {
        if (a[i] != b[i]) {
            d.pb(i);
        }
    }
    
    if (d.empty()) {
        cout << 0 << endl;
        return;
    }
    
    int c1 = 0;
    for (int i : d) {
        if (a[i] == 1) {
            c1++;
        }
    }
    
    if (c1 % 2 == 1) {
        cout << 1 << endl;
        return;
    }
    
    if (c1 > 0 && c1 % 2 == 0) {
        cout << 2 << endl;
        return;
    }
    
    int o1 = 0, o0 = 0;
    rep(i, 0, n) {
        if (a[i] == b[i]) {
            if (a[i] == 1) o1++;
            else o0++;
        }
    }
    
    if (o1 == 0 || o0 == 0) {
        cout << -1 << endl;
    } else {
        cout << 2 << endl;
    }
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
