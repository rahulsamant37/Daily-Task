/*
Author: Baldy Cape
Created: 2026-02-20 22:18:33
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(x) (int)(x).size()
#define rep(i, a, b) for(int i = (a); i < (b); ++i)
#define per(i, a, b) for(int i = (b) - 1; i >= (a); --i)
#define endl '\n'

#ifdef LOCAL
#define debug(x) cerr << "[DEBUG] " << #x << " = " << (x) << endl
#define debug2(x, y) cerr << "[DEBUG] " << #x << " = " << (x) << ", " << #y << " = " << (y) << endl
#else
#define debug(x)
#define debug2(x, y)
#endif

const int MOD = 1e9 + 7;
const int MOD2 = 998244353;
const ll INF = 1e18;
const int MAXN = 2e5 + 5;

void setup_io() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
}

ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
ll lcm(ll a, ll b) { return a / gcd(a, b) * b; }

ll pow_mod(ll base, ll exp, ll mod = MOD) {
    ll result = 1;
    base %= mod;
    while(exp > 0) {
        if(exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}

ll mod_inv(ll a, ll mod = MOD) {
    return pow_mod(a, mod - 2, mod);
}

struct DSU {
    vi parent, rank, size;
    int components;
    
    DSU(int n) : parent(n), rank(n, 0), size(n, 1), components(n) {
        iota(all(parent), 0);
    }
    
    int find(int x) {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    }
    
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if(x == y) return false;
        if(rank[x] < rank[y]) swap(x, y);
        parent[y] = x;
        size[x] += size[y];
        if(rank[x] == rank[y]) rank[x]++;
        components--;
        return true;
    }
    
    int get_size(int x) { return size[find(x)]; }
    int get_components() { return components; }
};


// O(n**2) time Complexity worst case
int main() {
    setup_io();
    
    int n;
    cin >> n;
    vi arr(n);
    rep(i, 0, n) cin >> arr[i];
    rep(i, 0, n) {
        rep(j, i+1, n) {
            if (arr[i]>arr[j]) swap(arr[i], arr[j]);
        }
    }
    rep(i,0,n) cout << arr[i] << " ";
    
    return 0;
}