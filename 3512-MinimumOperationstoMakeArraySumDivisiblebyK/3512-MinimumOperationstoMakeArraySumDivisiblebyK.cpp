// Last updated: 29/11/2025, 7:20:06 am
1class Solution {
2public:
3    int minOperations(vector<int>& nums, int k) {
4        return accumulate(nums.begin(), nums.end(), 0) % k;
5    }
6};