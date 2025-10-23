#include <iostream>
using namespace std;

int main() {
    int marks;
    cin >> marks;
    if (marks<35 && marks>=0) {
        cout << "F" << endl;
    }
    else if (marks>=35 && marks <50) {
        cout << "E" << endl;
    }
    else if (marks>=50 && marks <60) {
        cout << "D" << endl;
    }
    else if (marks>=60 && marks<70) {
        cout << "C" << endl;
    }
    else if (marks>=70 && marks <85) {
        cout << "B" << endl;
    }
    else if (marks>=85 && marks<=100) {
        cout << "A" << endl;
    }
    else {
        cout << "Enter a Valid marks!" << endl;
    }
}