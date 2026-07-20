#include <chrono>
#include <cstdint>
#include <iostream>

std::chrono::seconds f_chrono(std::chrono::seconds x, std::chrono::seconds y) {
    return x + y;
}

int64_t f_c(int64_t x, int64_t y) {
    return x + y;
}

int main(int argc, char* argv[]) {
    std::chrono::seconds a{1};
    std::cout << f_chrono(a, std::chrono::seconds {1}) << std::endl;
    int64_t b = 1;
    std::cout << f_c(b, 1) << std::endl;
    return 0;
}
