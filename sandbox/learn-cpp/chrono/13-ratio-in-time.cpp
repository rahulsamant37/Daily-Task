#include <cstdint>
#include <numeric>
#include <iostream>
#include <ratio>

template <intmax_t N, intmax_t D = 1>
class ratio {
    static constexpr intmax_t gcd_ = std::gcd(N, D);
public:
    static constexpr intmax_t num = N / gcd_; // N/D reduced to
    static constexpr intmax_t den = D / gcd_; // lowest terms
    using type = ratio<num, den>;
};

using nano = std::ratio<1, 1'000'000'000>;
using micro = std::ratio<1,    1'000'000>;
using milli = std::ratio<1,        1'000>;

int main(int argc, char* argv[]) {
    // Using std::ratio aliases
    std::cout << "nano = " << nano::num << "/" << nano::den << '\n';
    std::cout << "micro = " << micro::num << "/" << micro::den << '\n';
    std::cout << "milli = " << milli::num << "/" << milli::den << '\n';
    
    return 0;
}
