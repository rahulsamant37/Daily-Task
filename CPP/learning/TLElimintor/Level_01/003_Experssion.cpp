#include <iostream>
using namespace std;

// 1. "(expr1) && (expr2)" checks whether BOTH are true
// 2. "(expr1) || (expr2)" checks whether EITHER one is true
// 3. "!(expr)" return the OPPOSITE of the result of "expr"

int main() {
    cout << ((5<6) && (6<5)) << endl; // false -> 0
    cout << ((5<6) || (6<5)) << endl; // true -> 1
    cout << (!(5<6)) << endl; // (!(true)) = false -> 0
}