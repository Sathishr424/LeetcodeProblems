// Last updated: 19/11/2025, 6:44:37 am
class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int> set;
        for (int num: nums) {
            set.insert(num);
        }

        while (set.find(original) != set.end()) {
            original *= 2;
        }

        return original;
    }
};