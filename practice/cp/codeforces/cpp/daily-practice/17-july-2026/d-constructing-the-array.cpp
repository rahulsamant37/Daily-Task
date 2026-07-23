/*
Author: Rahul Samant
Created: 2026-07-23 12:40:15
*/

#include <bits/stdc++.h>
#include <functional>
#include <queue>
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

template<typename T>
void show_all(std::string_view rem, const T& v)
{
    std::cout << rem << ": ";
    for (const auto& e : v)
        std::cout << e << ' ';
    std::cout << '\n';
}

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
    vi arr(n, 0);
    priority_queue<pair<int, pii>, vector<pair<int, pii>>, greater<pair<int, pii>>> pq;
    pq.push({-n, {1, n}});
    int cnt = 1;
    while (!pq.empty()) {
        int l = pq.top().second.first;
        int r = pq.top().second.second;
        pq.pop();
        int mid = (l+r)/2;
        arr[mid-1] = cnt++;
        if (l==r) continue;
        if (l<mid){
            pq.push({-(mid-l), {l, mid-1}});
        }
        if (mid<r) {
            pq.push({-(r-mid), {mid+1, r}});
        }

    }
    rep(i, 0, n) { cout << arr[i] << " ";}
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
