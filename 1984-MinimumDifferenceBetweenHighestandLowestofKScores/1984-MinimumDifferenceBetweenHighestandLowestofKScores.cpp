// Last updated: 1/25/2026, 12:30:15 PM
1
2class Solution {
3public:
4  int minimumDifference(vector<int> &nums, int k) {
5    int n = nums.size();
6
7    sort(nums.begin(), nums.end());
8    int best = INT_MAX;
9
10    for (int i = 0; i < n - k + 1; i++) {
11      best = min(best, nums[i + k - 1] - nums[i]);
12    }
13
14    return best;
15  }
16};
17