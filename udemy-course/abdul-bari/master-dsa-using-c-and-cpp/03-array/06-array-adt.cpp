#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

struct Array {
    int *A;
    int size;
    int length;
};

void display(struct Array arr) {
    int i;
    cout << "\nElemets are: \n";
    for (i=0; i<arr.size; i++) {
        cout << arr.A[i] << " ";
    }
    cout << endl;
}

void appen(struct Array &arr, int x) {
    if (arr.length<arr.size) {
        arr.A[arr.length++] = x;
    }
}

void inser(struct Array &arr,int index, int x) {
    if(index>=0 && index <=arr.length) {
        for (int i=arr.length;i>index; i--) {
            arr.A[i] = arr.A[i-1];
        }
        arr.A[index] = x;
        arr.length++;
    }
}

void delet(struct Array &arr, int index) {
    if (index>=0 && index<arr.length) {
        for (int i = index; i < arr.length; i++) {
            arr.A[i] = arr.A[i+1];
        }
        arr.length--;
    }
}

int main() {
    struct Array arr;
    int n, i;
    cout << "Enter Size of an Array: \n";
    cin >> arr.size;
    arr.A = new int[arr.size];
    arr.length = 0;
    cout << "Enter number of numbers: \n";
    cin >> n;
    cout << "Enter all elements: \n";
    for (i = 0; i < n; i++) {
        cin >> arr.A[i];
    }
    arr.length = n;
    cout << "Given Array ";
    display(arr);
    appen(arr, 10);
    cout << "after appending ";
    display(arr);
    inser(arr, 0, 0);
    cout << "after inserting ";
    display(arr);
    delet(arr, 5);
    cout << "after deleting ";
    display(arr);

    delete[] arr.A;

    return 0;
}
