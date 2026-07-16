/*
Author: Rahul Samant
Created: 2026-07-16 19:27:47
*/

#include <bits/stdc++.h>
#include <unordered_set>
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
    ll n;
    cin >> n;
    vector<ll> arr(2*n);
    rep(i, 0, 2*n) cin >> arr[i];
    unordered_set<ll> arr2;
    ll maxi = 0;
    for(ll i: arr) {
        if (!arr2.empty() && arr2.find(i)!=arr2.end()) {
            arr2.erase(i);
        } else {
            arr2.insert(i);
        }
        ll curr = arr2.size();
        maxi = max(maxi, curr);
    }
    cout << maxi;
    return 0;
}
