// Last updated: 17/11/2025, 11:44:35 am
class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int prev_one = -(k + 1);
        int n = nums.size();
        for (int i=0; i<n; i++) {
            if (nums[i] == 1) {
                if (i - prev_one <= k) return false;
                prev_one = i;
            }
        }
        return true;
    }
};