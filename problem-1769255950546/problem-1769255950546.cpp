// Last updated: 1/24/2026, 5:29:10 PM
1class Solution {
2public:
3  int minPairSum(vector<int> &nums) {
4    int n = nums.size();
5    sort(nums.begin(), nums.end());
6
7    int l = 0;
8    int r = n-1;
9    int maxNum = 0;
10
11    while (l < r) {
12      maxNum = max(maxNum, nums[l] + nums[r]);
13      l++;
14      r--;
15    }
16
17    return maxNum;
18  }
19};
20