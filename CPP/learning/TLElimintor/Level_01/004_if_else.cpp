#include <iostream>
using namespace std;

// int main() {
//     int x = 5;
//     int y = 7;
//     int z = 10;

//     if (x<y && y<z) {
//         cout << "Y is in between" << endl;
//     } else {
//         cout << "Y is not in between" << endl;
//     }
// }

int main() {
    int age; cin >> age;
    bool disabled; cin >> disabled;

    if (age>65) {
        cout << "Senior Citizen Benefits" << endl;
    } else if (disabled) {
        cout << "Diabled benefits" << endl;
    } else {
        cout << "No benefits" << endl;
    }
}