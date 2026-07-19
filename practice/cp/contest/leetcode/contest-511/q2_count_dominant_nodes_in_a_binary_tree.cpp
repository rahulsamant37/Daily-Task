#include <algorithm>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    int ans = 0;
    
    int dfs(TreeNode* root) {
        if (!root) return 0;
        
        int l = dfs(root->left);
        int r = dfs(root->right);
        
        int mx = max(root->val, max(l, r));
        
        if (root->val == mx) {
            ans++;
        }
        
        return mx;
    }

public:
    int countDominantNodes(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
