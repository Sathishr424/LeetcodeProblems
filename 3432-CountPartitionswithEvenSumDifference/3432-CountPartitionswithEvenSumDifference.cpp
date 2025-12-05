// Last updated: 12/5/2025, 11:45:12 PM
1class Solution {
2public:
3    int countPartitions(vector<int>& nums) {
4        int right = accumulate(nums.begin(), nums.end(), 0);
5        int left = 0;
6        int count = 0;
7        for (int i=0; i<nums.size() - 1; i++) {
8            left += nums[i];
9            right -= nums[i];
10            
11            if (abs(left - right) % 2 == 0) {
12                count++;
13            }
14        }
15        return count;
16    }
17};