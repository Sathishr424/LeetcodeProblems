// Last updated: 10/11/2025, 7:25:20 pm
#include <iostream>
#include <ostream>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    static int minimumDistance(vector<int>& nums) {
        unordered_map<int, vector<int>> indexes;

        int min_diff = INT_MAX;
        for (int index = 0; index < nums.size(); index++) {
            if (indexes.find(nums[index]) == indexes.end()) {
                indexes[nums[index]] = vector<int>();
            }
            vector<int>& curr_nums = indexes[nums[index]];
            curr_nums.push_back(index);
            if (curr_nums.size() >= 3) {
                int n = curr_nums.size();
                int k = curr_nums[n - 1];
                int j = curr_nums[n - 2];
                int i = curr_nums[n - 3];
                min_diff = min(min_diff, (j - i) + (k - j) + (k - i));
            }
        }

        return min_diff == INT_MAX ? -1 : min_diff;
    }
};