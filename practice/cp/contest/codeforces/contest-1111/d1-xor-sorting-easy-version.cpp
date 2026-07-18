/*
Author: Rahul Samant
Created: 2026-07-18 21:51:00
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
    int n, q;
    cin >> n >> q;
    vi a(n);
    rep(i, 0, n) cin >> a[i];
    
    for (int p = 19; p >= 0; --p) {
        int len = 1 << p;
        bool found = false;
        for (int start = 0; start < n; start += (len * 2)) {
            int mid = start + len;
            int end = min(n, start + len * 2);
            if (mid >= n) continue;
            int mx = -1;
            rep(i, start, mid) {
                if (a[i] > mx) mx = a[i];
            }
            int mn = 2e9 + 7;
            rep(i, mid, end) {
                if (a[i] < mn) mn = a[i];
            }
            if (mx > mn) {
                found = true;
                break;
            }
        }
        if (found) {
            cout << (1 << p) << endl;
            return;
        }
    }
    
    cout << 0 << endl;
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
