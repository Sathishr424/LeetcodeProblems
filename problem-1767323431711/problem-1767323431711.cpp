// Last updated: 1/2/2026, 8:40:31 AM
1class Solution {
2public:
3    int repeatedNTimes(vector<int>& nums) {
4        int n = nums.size();
5        int half = n / 2;
6        
7        for (int i=2; i<n; i+=2) {
8            if (nums[i] == nums[i - 2]) return nums[i];
9        }
10
11        for (int i=3; i<n; i+=2) {
12            if (nums[i] == nums[i - 2]) return nums[i];
13        }
14
15        for (int i=0; i<n; i++) {
16            if (nums[i] == nums[(i - 1 + n) % n]) return nums[i];
17        }
18
19        return -1;
20    }
21};