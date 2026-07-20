#include <bits/stdc++.h>
#include <chrono>
#define endl '\n'

int main() {
    // std::chrono::seconds s = 3; // error: Not implicity constructible from int
    std::chrono::seconds s{3};
    std::cout << s << endl; // output - 3s
    std::cout << s.count() << endl; // output - 3
    return 0;
}
