/*
Author: Baldy Cape
Created: 2026-02-21 00:45:49
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

void print_vi(int arr[], int n) {
    rep(i, 0, n) {
        cout << arr[i] << " ";
    }
}

int main() {
    setup_io();
    int arr[] = {100, 20, 30, 10, 40, 50};
    int size = sizeof(arr) / sizeof(arr[0]);
    sort(arr, arr+size); // ascending
    print_vi(arr, size);
    cout << endl;
    sort(arr, arr+size, greater<int>()); // descending
    // reverse(arr.begin(), arr.end()); // another way to reverse
    print_vi(arr, size);
    
    return 0;
}