// Last updated: 12/25/2025, 7:11:35 PM
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        return accumulate(nums.begin(), nums.end(), 0) % k;
    }
};