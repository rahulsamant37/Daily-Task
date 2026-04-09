#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

void printArray(int (*ptr)[5], int size) {
    for (int i = 0; i < size; i++)
        cout << (*ptr)[i] << " ";
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    int arr[5] = {10, 20, 30, 40, 50};

    // Pointer to the whole array (type: int (*)[5])
    int (*ptrToArr)[5] = &arr;

    // Access entire array address vs first element address
    cout << "Address of array  : " << ptrToArr << endl;
    cout << "Address of arr[0] : " << *ptrToArr << endl;

    // Dereferencing gives back the array → index into it
    cout << "First element  : " << (*ptrToArr)[0] << endl;
    cout << "Third element  : " << (*ptrToArr)[2] << endl;

    // Pointer arithmetic on array pointer jumps the WHOLE array size
    cout << "Next array addr: " << (ptrToArr + 1) << endl;  // jumps 5*4 = 20 bytes ahead

    // Traverse using pointer to array
    cout << "All elements   : ";
    for (int i = 0; i < 5; i++)
        cout << (*ptrToArr)[i] << " ";
    cout << endl;

    // Pass pointer-to-array to a function
    cout << "Via function   : ";
    printArray(ptrToArr, 5);

    // 2D array — pointer to array shines here
    int matrix[3][4] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
    int (*row)[4] = matrix;   // points to first row

    cout << "\nMatrix row by row:\n";
    for (int i = 0; i < 3; i++, row++) {
        for (int j = 0; j < 4; j++)
            cout << (*row)[j] << "\t";
        cout << endl;
    }

    return 0;
}
