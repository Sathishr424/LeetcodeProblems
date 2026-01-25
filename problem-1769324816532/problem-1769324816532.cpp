// Last updated: 1/25/2026, 12:36:56 PM
1
2class Solution {
3public:
4  int minimumPrefixLength(vector<int> &nums) {
5    int n = nums.size();
6
7    vector<int> increasing(n, 0);
8    increasing[n - 1] = 1;
9
10    for (int i = n - 2; i >= 0; i--) {
11      if (nums[i] < nums[i + 1]) {
12        increasing[i] = increasing[i + 1] + 1;
13      } else
14        increasing[i] = 1;
15    }
16
17    for (int i = 0; i < n; i++) {
18      if (increasing[i] == n - i)
19        return i;
20    }
21
22    return n;
23  }
24};
25