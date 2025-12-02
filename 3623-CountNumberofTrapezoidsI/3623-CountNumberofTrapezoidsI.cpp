// Last updated: 2/12/2025, 4:41:57 pm
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
14            if (it.second <= 1) continue;
15            long long curr = it.second * 1LL * (it.second - 1) / 2;
16            ans = (ans + prev * curr % mod) % mod;
17            prev += curr;
18        }
19
20        return ans;
21    }
22};