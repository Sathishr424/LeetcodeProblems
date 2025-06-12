// Last updated: 12/6/2025, 5:54:56 am
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int pos = nums.size()-1;
        for (int i=0; i<nums.size(); i++){
            if (nums[i] == val){
                nums[i] = nums[pos];
                pos--; i--;
            }if (i >= pos) break;
        }return pos+1;
    }
};