#include <chrono>
#include <iostream>

constexpr std::chrono::seconds time_limit{2};

void f(std::chrono::seconds d) {
    if (d<=time_limit) {
        std::cout << "in time(" << time_limit << "): ";
    } else {
        std::cout << "out of time(" << time_limit << "): ";
    }
    std::cout << d << std::endl;
}

int main(int argc, char* argv[]) {
    f(std::chrono::seconds {1});
    f(std::chrono::seconds {3});
    return 0;
}
