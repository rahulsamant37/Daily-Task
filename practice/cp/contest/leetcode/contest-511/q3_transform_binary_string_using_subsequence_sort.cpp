#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<bool> canTransform(string s, vector<string>& strs) {
        vector<int> pos_s;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '0') {
                pos_s.push_back(i);
            }
        }
        
        int c = pos_s.size();
        vector<bool> ans(strs.size());
        
        for (int i = 0; i < strs.size(); i++) {
            int c0 = 0, cq = 0;
            for (char ch : strs[i]) {
                if (ch == '0') c0++;
                else if (ch == '?') cq++;
            }
            
            if (c0 > c || c0 + cq < c) {
                ans[i] = false;
                continue;
            }
            
            int need = c - c0;
            bool ok = true;
            int ptr = 0;
            
            for (int j = 0; j < strs[i].length(); j++) {
                if (strs[i][j] == '0') {
                    if (j > pos_s[ptr++]) {
                        ok = false;
                        break;
                    }
                } else if (strs[i][j] == '?' && need > 0) {
                    if (j > pos_s[ptr++]) {
                        ok = false;
                        break;
                    }
                    need--;
                }
            }
            ans[i] = ok;
        }
        
        return ans;
    }
};
