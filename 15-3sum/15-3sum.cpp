// Last updated: 12/6/2025, 5:55:20 am
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums){
        std::vector<vector<int>> ret;
        if (nums.size() == 0) return ret;
        sort(nums.begin(), nums.end());
        std::size_t n_size = nums.size();
        for (int i=0; i<n_size; i++){
            if (nums[i] > 0) break;

            if (i > 0 && nums[i] == nums[i-1]) continue;

            int left = i+1, right=n_size-1;
            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0) right--;
                else if (sum < 0) left++;
                else{
                    ret.push_back({nums[i], nums[left], nums[right]});
                    int lastLeft = left, lastRight = right;
                    while (left < right && nums[left] == nums[lastLeft]) left++;
                    while (left < right && nums[right] == nums[lastRight]) right--;
                }
            }

        }
        return ret;
    }
};