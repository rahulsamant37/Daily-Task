#include <chrono>
#include <iostream>
using namespace std::chrono_literals;

int main(int argc, char* argv[]) {
    // std::chrono::seconds x = 3400ms; // error: no conversion
    std::chrono::seconds x = std::chrono::duration_cast<std::chrono::seconds>(3400ms); // 3s
    std::cout << x << std::endl;
    return 0;
}
