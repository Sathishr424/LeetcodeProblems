// Last updated: 2/12/2025, 5:46:06 pm
1class Solution {
2public:
3    int countTrapezoids(vector<vector<int>>& points) {
4        int mod = 1e9 + 7;
5        unordered_map<int, int> slopes;
6
7        for (auto& cord: points) {
8            slopes[cord[1]]++;
9        }
10
11        int ans = 0;
12        int prev = 0;
13        for (auto& it: slopes) {
14            long long curr = it.second * 1LL * (it.second - 1) / 2;
15            ans = (ans + prev * curr % mod) % mod;
16            prev += curr;
17        }
18
19        return ans;
20    }
21};