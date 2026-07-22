#include <chrono>
#include <iostream>
using namespace std::chrono_literals;

void f(std::chrono::nanoseconds d) {
    std::cout << d.count() << "ns\n";
}

int main(int argc, char* argv[]) {
    auto x = 2h;
    auto y = 3us;
    f(x+y); // 7200000003000ns
    return 0;
}
