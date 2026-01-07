// Last updated: 1/7/2026, 6:42:24 PM
1
2int dfs(TreeNode *node, long long &totalSum, long long &ans) {
3  if (node == nullptr)
4    return 0;
5
6  long long left = dfs(node->left, totalSum, ans);
7  long long right = dfs(node->right, totalSum, ans);
8
9  long long currSum = left + right + node->val;
10  long long rem = totalSum - currSum;
11  long long currAns = currSum * 1LL * rem;
12
13  if (rem > 0 && currAns > ans) {
14    ans = currAns;
15  }
16
17  return currSum;
18}
19int mod = 1e9 + 7;
20class Solution {
21public:
22  int maxProduct(TreeNode *root) {
23    vector<TreeNode *> stack;
24
25    stack.push_back(root);
26    long long totalSum = 0;
27    while (stack.size() > 0) {
28      TreeNode *node = stack.back();
29      stack.pop_back();
30      totalSum += node->val;
31      if (node->left)
32        stack.push_back(node->left);
33      if (node->right)
34        stack.push_back(node->right);
35    }
36
37    long long ans = 0;
38
39    dfs(root, totalSum, ans);
40    return ans % mod;
41  }
42};
43