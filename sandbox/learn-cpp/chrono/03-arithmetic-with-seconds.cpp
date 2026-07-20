#include <chrono>
#include <iostream>
using namespace std::chrono_literals;

void f(std::chrono::seconds d) {
    std::cout << d << std::endl;
}

int main(int argc, char* argv[]) {
    auto x = 1s;
    f(x);
    x+=2s;
    f(x);
    x = x - 1s;
    f(x);
    // f(x+1); // error: seconds + int not allowed
    f(x + 1s);
    return 0;
}
