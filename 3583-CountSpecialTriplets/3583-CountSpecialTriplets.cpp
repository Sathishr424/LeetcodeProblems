// Last updated: 12/9/2025, 6:17:23 AM
1class Solution {
2public:
3    int specialTriplets(vector<int>& nums) {
4        int n = nums.size();
5        int mod = 1e9 + 7;
6
7        unordered_map<int, int> right;
8        unordered_map<int, int> left;
9
10        for (int num: nums) {
11            right[num]++;
12        }
13
14        int ans = 0;
15        for (int num: nums) {
16            right[num]--;
17
18            int need = num * 2;
19            ans += (left[need] * 1LL * right[need]) % mod;
20            ans %= mod;
21            
22            left[num]++;
23        }
24
25        return ans;
26    }
27};