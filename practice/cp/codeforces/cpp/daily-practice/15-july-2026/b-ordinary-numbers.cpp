/*
Author: Rahul Samant
Created: 2026-07-15 22:32:13
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
    ll n;
    cin >> n;
    string str = to_string(n);
    int len = str.size();
    int first = str[0] - '0';
    ll comp = 0;
    for (int i = 0; i<len; i++) {
        comp = comp * 10 + first;
    }
    int ans = 9 * (len - 1);
    if(comp<=n) {
        ans+=first;
    } else {
        ans+=first-1;
    }
    cout << ans << endl;
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
