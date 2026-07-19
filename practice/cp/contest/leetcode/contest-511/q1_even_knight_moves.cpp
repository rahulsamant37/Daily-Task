#include <vector>

using namespace std;

class Solution {
public:
    bool canReach(vector<int>& start, vector<int>& target) {
        int s_parity = (start[0] + start[1]) % 2;
        int t_parity = (target[0] + target[1]) % 2;
        
        return s_parity == t_parity;
    }
};
