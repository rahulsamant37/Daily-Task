/*
author: rahul samant
created: 2026-06-20 18:10:21
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
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define endl '\n'

#ifdef local
#define debug(x) cerr << "[debug] " << #x << " = " << (x) << endl
#else
#define debug(x)
#endif

const int mod = 1e9 + 7;
const ll inf = 1e18;

void setup_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
#ifdef local
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

int main() {
    setup_io();
    int n;
    cin >> n;

    vector<pair<long long, long long>> a(n);

    for (int i = 0; i < n; i++) {
        long long h, l;
        cin >> h >> l;
        a[i] = {l, h};
    }

    sort(a.begin(), a.end());

    vector<long long> suf(n);
    suf[n - 1] = a[n - 1].second;

    for (int i = n - 2; i >= 0; i--) {
        suf[i] = max(suf[i + 1], a[i].second);
    }

    int q;
    cin >> q;

    while (q--) {
        long long t;
        cin >> t;

        int pos = upper_bound(
            a.begin(),
            a.end(),
            make_pair(t, (long long)4e18)
        ) - a.begin();

        cout << suf[pos] << '\n';
    }
    return 0;
}
