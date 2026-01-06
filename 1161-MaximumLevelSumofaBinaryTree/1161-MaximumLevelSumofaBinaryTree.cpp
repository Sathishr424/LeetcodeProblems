// Last updated: 1/6/2026, 4:08:11 PM
1class Solution {
2public:
3  int maxLevelSum(TreeNode *root) {
4    unordered_map<int, int> levels;
5
6    function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int level) {
7      if (node == nullptr) return;
8
9      levels[level] += node->val;
10
11      dfs(node->left, level + 1);
12      dfs(node->right, level + 1);
13    };
14
15    dfs(root, 1);
16
17    int minLevel = 1;
18    for (auto& it: levels) {
19      if (levels[it.first] > levels[minLevel] || (levels[it.first] == levels[minLevel] && it.first < minLevel)) {
20        minLevel = it.first;
21      }
22    }
23
24    return minLevel;
25  }
26};