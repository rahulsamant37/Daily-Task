#include <iostream>
using namespace std;


//Two Sum
int main() {
    int arr[3] = {10, 20, 30};
    int target = 30;
    int l = 0;
    int r = sizeof(arr)/sizeof(arr[0]) - 1;
    while (l<=r) {
        int m = (l + r) / 2;
        if (arr[m]== target) {
            cout << "Found at index: " << m << endl;
            return 0;
        }
        else if (arr[m] < target)
        {
            l = m+1;
        }
        else {
            r = m-1;
        }
    }
    cout << "Not found" << endl;
    return 0;
}