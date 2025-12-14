// Last updated: 12/14/2025, 4:29:47 PM
1class Solution {
2public:
3    int absDifference(vector<int>& nums, int k) {
4        int n = nums.size();
5        sort(nums.begin(), nums.end());
6
7        int left = 0;
8        int right = 0;
9
10        for (int i=0; i<k; i++) left += nums[i];
11        for (int i=n-k; i<n; i++) right += nums[i];
12
13        return right - left;
14    }
15};