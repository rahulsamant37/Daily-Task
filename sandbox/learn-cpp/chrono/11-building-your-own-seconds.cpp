#include <chrono>
#include <cstdint>  
#include <iostream>
// #include <stdexcept>
// using namespace std::chrono_literals;
//
// struct safe_uint32_t {
//     uint32_t value;
//
//     safe_uint32_t(uint32_t v) : value(v) {}
//
//     safe_uint32_t operator+(const safe_uint32_t& other) const {
//         if (value > UINT32_MAX - other.value)
//             throw std::overflow_error("overflow");
//         return safe_uint32_t(value + other.value);
//     }
// };

// normal seconds uses
// using seconds = std::chrono::duration<long long>
using seconds32 = std::chrono::duration<int32_t>;
using secondsu32 = std::chrono::duration<uint32_t>;
using secondssafe32 = std::chrono::duration<safe_uint32_t>;

int main(int argc, char* argv[]) {
    seconds32 t(3);
    secondsu32 k(3);
    std::cout << t << std::endl;
    std::cout << k << std::endl;
    // secondssafe32 m(4'294'967'295); // max
    // // noramally wraps around to 0 (overflow!)
    // m += 1s;
    return 0;
}
