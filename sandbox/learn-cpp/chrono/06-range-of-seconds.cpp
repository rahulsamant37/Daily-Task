#include <chrono>
#include <iostream>

int main(int argc, char* argv[]) {
    std::chrono::seconds m = std::chrono::seconds::min();
    std::chrono::seconds M = std::chrono::seconds::max();
    std::cout << "========== In Seconds ==========" << std::endl;
    std::cout << m << std::endl;
    std::cout << M << std::endl;
    std::cout << "========== In Years ==========" << std::endl;
    std::cout << m.count()/31536000 << std::endl;
    std::cout << M.count()/31536000 << std::endl;
    
    return 0;
}
