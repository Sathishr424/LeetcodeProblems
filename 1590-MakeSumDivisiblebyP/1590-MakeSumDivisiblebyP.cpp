// Last updated: 30/11/2025, 7:35:10 am
1class Solution {
2public:
3    int minSubarray(vector<int>& nums, int p) {
4        int n = nums.size();
5
6        unordered_map<int, vector<int>> left;
7        left[0].push_back(-1);
8        int sum = 0;
9        for (int i=0; i<n; i++) {
10            sum += nums[i];
11            sum %= p;
12            left[sum].push_back(i);
13        }
14
15        int best = INT_MAX;
16        sum = 0;
17        for (int i=n-1; i>=0; i--) {
18            int need = (p - sum) % p;
19            if (left.find(need) != left.end()) {
20                while (!left[need].empty() && left[need].back() > i) {
21                    left[need].pop_back();
22                }
23                if (!left[need].empty()) {
24                    best = min(best, i - left[need].back());
25                }
26            }
27            sum += nums[i];
28            sum %= p;
29        }
30
31        return best == INT_MAX || best == n ? -1 : best;
32    }
33};