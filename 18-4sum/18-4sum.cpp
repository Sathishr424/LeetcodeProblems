// Last updated: 12/6/2025, 5:55:14 am
class Solution {
public:
    bool checkIf(vector<vector<int>> &total, vector<int> &x){
        for (unsigned int i=0; i<total.size(); i++){
            if (x == total[i]) return false;
        }return true;
    }
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ret;
        if (nums.size() <= 3) return ret;
        std::sort(nums.begin(), nums.end());
        std::size_t n = nums.size();
        for (unsigned int i=0; i<n-1; i++){
            for (unsigned int j=n-1; j>i+1; j--){
                unsigned int left = i+1, right = j-1;
                while (left < right){
                    unsigned int lastLeft = left, lastRight = right;
                    if (left != i && left != j && right != i && right != j){
                    int sum = nums[i] + nums[j] + nums[left] + nums[right];
                    if (target == sum) {vector<int> tmp = {nums[i], nums[left], nums[right],nums[j]};
                        if (checkIf(ret, tmp)) ret.push_back(tmp);
                    }
                    else if (sum - target < 0) {left++; continue;}
                    else if (sum - target > 0) {right--;continue;}
                    }
                    while (left < right && nums[left] == nums[lastLeft]) left++;
                    while (left < right && nums[right] == nums[lastRight]) right--;
                }
            }
        }return ret;
    }
};