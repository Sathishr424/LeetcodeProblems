// Last updated: 12/14/2025, 1:59:57 PM
1class Solution {
2public:
3    int numberOfWays(string corridor) {
4        int mod = 1e9 + 7;
5        int n = corridor.length();
6        vector<vector<int>> dp(n + 1, vector<int>(3, 0));
7        dp[0][0] = 1;
8
9        for (int i=0; i<n; i++) {
10            char c = corridor[i];
11            for (int s=0; s<=2; s++) {
12                if (c == 'S') {
13                    if (s == 2) {
14                        dp[i + 1][1] += dp[i][s];
15                        dp[i + 1][1] %= mod;
16                    } else {
17                        dp[i + 1][s + 1] += dp[i][s];
18                        dp[i + 1][s + 1] %= mod;
19                    }
20                } else {
21                    if (s == 2) {
22                        dp[i + 1][0] += dp[i][s];
23                        dp[i + 1][0] %= mod;
24                    }
25                    dp[i + 1][s] += dp[i][s];
26                    dp[i + 1][s] %= mod;
27                }
28            }
29        }
30
31        return dp[n][2];
32    }
33};