#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void printarr(char arr[ ], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    return;
} 

int main() {
    char temp;
    // to declare a character you needed to 
    // put it inside `'` single quotes only
    temp = 'A';
    int n = temp;
    cout << temp << endl;
    // cout << n << endl;
    cout << n << endl;

    // different ways to declare arr of strings
    char arrstr[5];
    char arrstr0[5] = {'A', 66};
    char arrstr1[5] = {'A', 'B', 'C', 'D', 'E'};
    char arrstr2[] = {'A', 'B', 'C', 'D', 'E'};
    char arrstr3[5] = {65, 66, 67, 68, 69};
    printarr(arrstr, 5);
    printarr(arrstr0, 5);
    printarr(arrstr1, 5);
    printarr(arrstr2, 5);
    printarr(arrstr3, 5);
    return 0;
}
