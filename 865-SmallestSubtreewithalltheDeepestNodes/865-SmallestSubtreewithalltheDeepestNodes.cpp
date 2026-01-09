// Last updated: 1/9/2026, 11:00:04 PM
1
2int dfs(TreeNode *node, unordered_map<int, int> &levels,
3        unordered_map<TreeNode *, int> &cnts, int level) {
4  if (node == nullptr)
5    return 0;
6
7  levels[level]++;
8  cnts[node] += 1;
9  cnts[node] += dfs(node->left, levels, cnts, level + 1);
10  cnts[node] += dfs(node->right, levels, cnts, level + 1);
11  return cnts[node];
12}
13
14int dfs2(TreeNode *node, unordered_map<TreeNode *, int> &deep_cnts, int level,
15         int deep_level) {
16  if (node == nullptr)
17    return 0;
18
19  deep_cnts[node] += (level == deep_level);
20  deep_cnts[node] += dfs2(node->left, deep_cnts, level + 1, deep_level);
21  deep_cnts[node] += dfs2(node->right, deep_cnts, level + 1, deep_level);
22
23  return deep_cnts[node];
24}
25
26class Solution {
27public:
28  TreeNode *subtreeWithAllDeepest(TreeNode *root) {
29    unordered_map<int, int> levels;
30    unordered_map<TreeNode *, int> cnts;
31
32    dfs(root, levels, cnts, 0);
33
34    int max_level = 0;
35
36    for (auto &it : levels)
37      max_level = max(max_level, it.first);
38    int max_level_cnt = levels[max_level];
39
40    unordered_map<TreeNode *, int> deep_cnts;
41
42    dfs2(root, deep_cnts, 0, max_level);
43    TreeNode *ans = nullptr;
44
45    for (auto &it : deep_cnts) {
46      TreeNode *node = it.first;
47      int cnt = it.second;
48
49      int node_cnt = cnts[node];
50
51      if (cnt == max_level_cnt && (ans == nullptr || node_cnt < cnts[ans])) {
52        ans = node;
53      }
54    }
55
56    return ans;
57  }
58};
59