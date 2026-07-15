#include <iostream>
#include <unordered_map>
#include <chrono>
#include <vector>

using namespace std;

// =====================================================================
// STEP 1: THE FIX (CUSTOM HASH)
// =====================================================================
// The splitmix64 function is a fast, high-quality hash function.
// The FIXED_RANDOM seed ensures that the hash function changes every 
// single time the program is executed.
struct custom_hash {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        // Generated exactly once per program run using the system clock
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        // Add the random seed, then scramble the bits thoroughly
        return splitmix64(x + FIXED_RANDOM);
    }
};

int main() {
    // We use 100,000 elements. In O(N^2) this is 10^10 operations,
    // which is more than enough to cause a visible delay (TLE).
    const int N = 100000; 
    
    // =====================================================================
    // STEP 2: CREATING THE MALICIOUS TEST CASE (THE HACK)
    // =====================================================================
    // We create a temporary map and reserve space for N elements.
    unordered_map<long long, int> temp_map;
    temp_map.reserve(N);
    
    // In C++, the bucket an integer 'x' goes into is (hash(x) % bucket_count).
    // Because the default hash(x) is just 'x', the bucket is simply (x % bucket_count).
    long long M = temp_map.bucket_count();
    cout << "Targeting bucket count: " << M << "\n\n";
    
    // If we insert numbers that are multiples of M (e.g., 0*M, 1*M, 2*M...),
    // they will ALL evaluate to: (i * M) % M = 0.
    // This forces EVERY single element into bucket 0, forming a massive linked list.
    vector<long long> malicious_data(N);
    for (int i = 0; i < N; ++i) {
        malicious_data[i] = i * M; 
    }

    // =====================================================================
    // STEP 3: RUNNING THE VULNERABLE MAP
    // =====================================================================
    cout << "--- 1. Testing Default unordered_map (Vulnerable) ---" << endl;
    unordered_map<long long, int> vulnerable_map;
    vulnerable_map.reserve(N); // Keep the bucket size constant at M
    
    auto start = chrono::high_resolution_clock::now();
    for (int i = 0; i < N; ++i) {
        // Normally O(1) time. 
        // But because of collisions, 1st element takes 1 step, 2nd takes 2, Nth takes N.
        // Total time becomes O(N^2), causing Time Limit Exceeded (TLE)!
        vulnerable_map[malicious_data[i]] = i;
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> diff_vuln = end - start;
    cout << "Time taken: " << diff_vuln.count() << " seconds.\n\n";

    // =====================================================================
    // STEP 4: RUNNING THE SAFE MAP WITH CUSTOM HASH
    // =====================================================================
    cout << "--- 2. Testing unordered_map with custom_hash (Safe) ---" << endl;
    unordered_map<long long, int, custom_hash> safe_map;
    safe_map.reserve(N); // Same initial conditions
    
    start = chrono::high_resolution_clock::now();
    for (int i = 0; i < N; ++i) {
        // Because we pass the number through splitmix64 + a random seed,
        // (hash(x) % M) scatters the numbers beautifully across all buckets.
        // It stays true O(1) on average.
        safe_map[malicious_data[i]] = i;
    }
    end = chrono::high_resolution_clock::now();
    chrono::duration<double> diff_safe = end - start;
    cout << "Time taken: " << diff_safe.count() << " seconds.\n\n";
    
    // =====================================================================
    // STEP 5: THE CONCLUSION
    // =====================================================================
    cout << "Speedup Factor: Safe map is roughly " 
         << (int)(diff_vuln.count() / diff_safe.count()) 
         << "x faster on malicious data!" << endl;

    return 0;
}
