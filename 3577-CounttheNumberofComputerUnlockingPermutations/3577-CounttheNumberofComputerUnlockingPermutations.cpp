// Last updated: 12/10/2025, 1:54:23 PM
1class Solution {
2public:
3    int countPermutations(vector<int>& c) {
4        int n = c.size();
5        int mod = 1e9 + 7;
6
7        int ans = 1;
8        for (int i=1; i<n; i++) {
9            if (c[i] <= c[0]) return 0;
10            ans = ans * 1LL * (n - i) % mod;
11        }
12
13        return ans;    
14    }
15};