#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int target, n;
    cin >> n >> target;
    int arr[n];
    for (int i = 0; i<n;i++) {
        cin >> arr[i];
        if (arr[i]==target) {
            cout << "Found it! it is at " << i << " index";
            return 0;
        }
    }
    cout << "It is not in the array";
    return 0;
}
