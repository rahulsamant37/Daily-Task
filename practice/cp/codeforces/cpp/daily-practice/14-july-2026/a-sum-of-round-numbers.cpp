/*
Author: Rahul Samant
Created: 2026-07-14 21:42:19
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
    int cnt = 0, idx = 0;
    vector<pair<int, int>> arr;
    while(n>0) {
        if (n%10!=0){
            cnt++;
            arr.push_back({n%10, idx});
        }
        idx++;
        n/=10;
    }
    cout << cnt << endl;
    for (unsigned long i = 0; i < arr.size(); i++) {
        int ans = (arr[i].first)*pow(10, arr[i].second);
        cout << ans << " ";
    }
    return;
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
