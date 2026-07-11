#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int arr[10] = {0,1,2,3,4,5,6,7,8,9};
    int l = 0, r=9,target;
    cin >> target;
    while (l<=r) {
        int mid = l + (r-l)/2;
        if (arr[mid] == target) {
            cout << "Found it! at index " << mid;
            return 0;
        } else if (arr[mid]<target) {
            r = mid-1;
        } else {
            l = mid+1;
        }
    }
    cout << "Not Found!";
    return 0;
}
