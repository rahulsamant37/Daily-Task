#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    int A[3][4] = {{1,2,3,4}, {5,6,7,8}, {9, 2, 4, 6}};
    int *B[3];
    int **C;

    B[0] = new int[4];
    B[1] = new int[4];
    B[2] = new int[4];

    C = new int*[3];
    C[0] = new int[4];
    C[1] = new int[4];
    C[2] = new int[4];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << A[i][j] << ' ';
        }
        cout << endl;
    }
    // Cleanup
    delete[] B[0];
    delete[] B[1];
    delete[] B[2];

    delete[] C[0];
    delete[] C[1];
    delete[] C[2];
    delete[] C;
    return 0;
}
