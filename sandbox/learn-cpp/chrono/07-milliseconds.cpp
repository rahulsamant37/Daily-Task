#include <chrono>
#include <iostream>

void f(std::chrono::milliseconds d) {
    std::cout << d << std::endl;
}

int main(int argc, char* argv[]) {
    f(std::chrono::milliseconds {3});
    f(std::chrono::seconds {2}); // ok, no change needed! 2000ms
    std::chrono::seconds x{1}; 
    f(x); // ok, no change needed! 1000ms
    return 0;
}
