// Last updated: 1/25/2026, 12:59:24 PM
1class Solution {
2public:
3  vector<int> rotateElements(vector<int> &nums, int k) {
4    vector<int> negIndexes;
5    int n = nums.size();
6    vector<int> ret(n, 0);
7
8    for (int i = 0; i < n; i++) {
9      if (nums[i] >= 0)
10        negIndexes.push_back(i);
11      else
12        ret[i] = nums[i];
13    }
14
15    int m = negIndexes.size();
16    for (int i = 0; i < m; i++) {
17      int index = negIndexes[i];
18      int newIndex = (i - k);
19      int diff = abs(min(0, newIndex));
20      int add = diff / m + 1;
21      newIndex = (newIndex + (m * 1LL * add)) % m;
22
23      ret[negIndexes[newIndex]] = nums[index];
24    }
25
26    return ret;
27  }
28};
29