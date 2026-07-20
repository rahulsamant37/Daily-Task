#include <bits/stdc++.h>
#include <chrono>
using namespace std::chrono_literals; // this is required to run f(4s);

#define endl '\n'

void f(std::chrono::seconds d) {
    std::cout << d << endl;
}

int main() {
    std::chrono::seconds s{3};
    // f(3); // error: Not implicitly constructible from int
    f(s);
    f(std::chrono::seconds{4});
    f(5s);
    return 0;
}
