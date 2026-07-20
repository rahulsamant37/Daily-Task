#include <chrono>
#include <iostream>

constexpr std::chrono::seconds time_limit{2};

void f(std::chrono::milliseconds d) {
    std::cout << d;
    if (d <= time_limit) {
        std::cout << " is In Time" << std::endl;
    } else {
        std::cout << " is Out of Time" << std::endl;
    }
}

int main(int argc, char* argv[]) {
    f(std::chrono::milliseconds(1));
    f(std::chrono::seconds(3)); // automatic conversion 3000ms
    
    return 0;
}
