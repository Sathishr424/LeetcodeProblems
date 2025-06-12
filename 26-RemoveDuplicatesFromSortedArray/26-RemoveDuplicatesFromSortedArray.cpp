// Last updated: 12/6/2025, 5:54:58 am
class Solution {
public:
    int removeDuplicates(vector<int>& nums){
        if (nums.size() <= 1) return nums.size();
        int ret = nums.size(), last = nums[0], cnt = 0;
        bool dup = 0;
        for (unsigned int i=1; i<nums.size(); i++){
            if (nums[i] == last) {nums.erase(nums.begin()+i); dup=1;}
            else last = nums[i];
            if (dup){
                i--;
                dup=0;
            }
        }return nums.size();
    }
};