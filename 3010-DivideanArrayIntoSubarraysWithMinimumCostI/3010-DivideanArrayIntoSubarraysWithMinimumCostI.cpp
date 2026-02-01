// Last updated: 2/1/2026, 12:49:04 PM
1class Solution {
2public:
3    int minimumCost(vector<int>& nums) {
4        int n = nums.size();
5        int best = INT_MAX;
6
7        for (int i=1; i<n-1; i++) {
8            for (int j=i+1; j<n; j++) {
9                best = min(best, nums[i] + nums[j] + nums[0]);
10            }
11        }
12        
13        return best;
14    }
15};