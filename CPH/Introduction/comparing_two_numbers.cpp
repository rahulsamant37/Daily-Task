/*
Author: Baldy Cape
Created: 2026-02-16

Description:
------------
Demonstrates floating-point precision issues in C++.
Shows why direct comparison (x == 1.0) fails and how to
properly compare floating-point numbers using an epsilon tolerance.

Concept:
--------
Due to binary representation limits, many decimal numbers
(e.g., 0.1, 0.3) cannot be stored exactly in a double.
Therefore, arithmetic operations may introduce tiny rounding errors.

Correct approach:
-----------------
Use a tolerance-based comparison:
    abs(a - b) < epsilon
*/

#include <iostream>
#include <cmath>

using namespace std;

/*
Function: areAlmostEqual
------------------------
Safely compares two double values using an epsilon tolerance.

Parameters:
    a       - First floating-point number
    b       - Second floating-point number
    epsilon - Allowed tolerance (default = 1e-9)

Returns:
    true  -> if numbers are approximately equal
    false -> otherwise
*/
bool areAlmostEqual(double a, double b, double epsilon = 1e-9) {
    return fabs(a - b) < epsilon;
}

/*
Function: demonstrateFloatingPointComparison
--------------------------------------------
Performs a floating-point computation and demonstrates
both incorrect (direct) and correct (epsilon-based) comparisons.
*/
void demonstrateFloatingPointComparison() {
    double x = 0.3 * 3 + 0.1;

    cout << "Computed value of x: " << x << endl;

    // ❌ Incorrect comparison
    if (x == 1.0) {
        cout << "Direct comparison works\n";
    } else {
        cout << "Direct comparison fails\n";
    }

    // ✅ Correct comparison
    if (areAlmostEqual(x, 1.0)) {
        cout << "Epsilon comparison works\n";
    } else {
        cout << "Epsilon comparison fails\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    demonstrateFloatingPointComparison();

    return 0;
}
