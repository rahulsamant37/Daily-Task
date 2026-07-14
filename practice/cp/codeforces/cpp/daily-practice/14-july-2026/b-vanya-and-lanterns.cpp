/*
Author: Rahul Samant
Created: 2026-07-14 19:34:22
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

int main() {
    setup_io();
    ll n, l;
    cin >> n >> l;
    vector<ll> arr(n);
    rep(i, 0, n) cin >>arr[i];
    sort(arr.begin(), arr.end());
    long double maxi = (long double)arr[0];
    rep(i, 1, n) {
        long double cur = (arr[i] - arr[i-1])/2.0;
        maxi = max(maxi, cur);
    }
    if (arr[n-1]!=l) {
        long double cur = l - arr[n-1];
        maxi = max(maxi, cur);
    }
    cout << std::fixed << std::setprecision(10);
    cout << maxi;
    return 0;
}
