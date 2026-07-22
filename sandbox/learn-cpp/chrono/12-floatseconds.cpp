#include <chrono>
#include <iostream>

using fseconds = std::chrono::duration<float>;
// using nanoseconds = duration<int_least64_t, nano>;
// using microseconds = duration<int_least55_t, micro>;
// using milliseconds = duration<int_least45_t, milli>;
// using seconds = duration<int_least35_t            >;

void f(fseconds d) {
    std::cout << d.count() << "s\n";
}

int main(int argc, char* argv[]) {
    /* 
     For floating-point representations, you can implicitly 
     convert from any precision without using duration_cast. 
     The rationale is that there is no truncation error 
     (only rounding error). And so implicit conversion is safe.
    */
    f(std::chrono::milliseconds (45) + std::chrono::microseconds (63)); // 0.045063s
    return 0;
}
