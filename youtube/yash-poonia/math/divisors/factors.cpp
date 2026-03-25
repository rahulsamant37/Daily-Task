/*
-----------------------------------------
Time Complexity:
-----------------------------------------
The loop runs from 1 to sqrt(n).

So the time complexity is:
    O(sqrt(n))

-----------------------------------------
Space Complexity:
-----------------------------------------
We store all divisors in a vector.
In the worst case, a number can have up to O(sqrt(n)) divisors.

So space complexity is:
    O(sqrt(n))

-----------------------------------------
Working Range of n:
-----------------------------------------
Since the algorithm runs in O(sqrt(n)) time:

- If n ≤ 10^12, sqrt(n) ≤ 10^6 → very fast
- If n ≤ 10^18, sqrt(n) ≤ 10^9 → too slow

Practically safe range:
    n up to 10^12 works comfortably.
    For competitive programming, n up to 10^9 is extremely safe.
*/


#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    // Value whose divisors we want to find
    int n = 12;

    // Vector to store all divisors of n
    vector<long long> divisors;

    /*
        We iterate from 1 to sqrt(n).
        If i divides n, then:
            - i is a divisor
            - n/i is also a divisor (if different)

        This avoids checking all numbers from 1 to n.
    */
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            divisors.push_back(i);

            // Avoid duplicate when i == n/i (perfect square case)
            if (i != n / i) {
                divisors.push_back(n / i);
            }
        }
    }

    // Number of divisors found
    int m = divisors.size();

    // Print all divisors
    for (int i = 0; i < m; i++) {
        cout << divisors[i] << " ";
    }

    return 0;
}
