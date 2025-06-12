// Last updated: 12/6/2025, 5:55:15 am
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target){
        if (nums.size() < 3) return 0;
        int ret = INT_MAX;
        std::size_t n = nums.size();
        std::sort(nums.begin(), nums.end());
        for (int i=0; i<n; i++){
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int left = i+1, right = n-1;
            while (left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if (sum < target){
                    left++;
                }else if (sum > target){
                    right--;
                }else{
                    return sum;
                }if (ret == INT_MAX || (abs(sum - target) < abs(ret - target))) ret = sum;
            }
        }return ret;
    }
};