// Last updated: 12/25/2025, 7:11:09 PM
class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        int mod = 1e9 + 7;
        unordered_map<int, int> slopes;

        for (auto& cord: points) {
            slopes[cord[1]]++;
        }

        int ans = 0;
        int prev = 0;
        for (auto& it: slopes) {
            long long curr = it.second * 1LL * (it.second - 1) / 2;
            ans = (ans + prev * curr % mod) % mod;
            prev += curr;
        }

        return ans;
    }
};