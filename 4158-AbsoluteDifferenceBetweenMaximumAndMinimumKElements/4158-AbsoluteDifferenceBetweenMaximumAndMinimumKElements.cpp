// Last updated: 12/25/2025, 7:07:51 PM
class Solution {
public:
    int absDifference(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        int left = 0;
        int right = 0;

        for (int i=0; i<k; i++) left += nums[i];
        for (int i=n-k; i<n; i++) right += nums[i];

        return right - left;
    }
};