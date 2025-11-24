// Last updated: 24/11/2025, 5:51:44 am
class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        int n = nums.size();
        int num = 0;
        vector<bool> ret;
        for (int i=0; i<n; i++) {
            num = num * 2 % 5;
            num = (num + nums[i]) % 5;
            ret.push_back(num == 0);
        }
        return ret;
    }
};