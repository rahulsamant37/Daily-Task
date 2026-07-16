/*
Author: Rahul Samant
Created: 2026-07-16 21:36:29
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
    if (n==1) {
        cout << 0 << endl;
        return;
    }
    ll cnt_two = 0, cnt_three = 0;
    while(n%2==0 || n%3==0) {
        if (n%2==0) {
            cnt_two++;
            n/=2;
        } else if (n%3==0) {
            cnt_three++;
            n/=3;
        }
    }
    if (n==1 && cnt_three>=cnt_two) {
        ll cnt = cnt_two + 2*(cnt_three - cnt_two);
        cout << cnt << endl;
        return;
    }
    cout << -1 << endl;
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
