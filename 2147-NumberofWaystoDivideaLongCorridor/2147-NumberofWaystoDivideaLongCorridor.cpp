// Last updated: 12/14/2025, 2:01:39 PM
1const int N = 1e5 + 1;
2int dp[N][3];
3
4class Solution {
5public:
6    int numberOfWays(string corridor) {
7        int mod = 1e9 + 7;
8        int n = corridor.length();
9        memset(dp, 0, sizeof(dp));
10        dp[0][0] = 1;
11
12        for (int i=0; i<n; i++) {
13            char c = corridor[i];
14            for (int s=0; s<=2; s++) {
15                if (c == 'S') {
16                    if (s == 2) {
17                        dp[i + 1][1] += dp[i][s];
18                        dp[i + 1][1] %= mod;
19                    } else {
20                        dp[i + 1][s + 1] += dp[i][s];
21                        dp[i + 1][s + 1] %= mod;
22                    }
23                } else {
24                    if (s == 2) {
25                        dp[i + 1][0] += dp[i][s];
26                        dp[i + 1][0] %= mod;
27                    }
28                    dp[i + 1][s] += dp[i][s];
29                    dp[i + 1][s] %= mod;
30                }
31            }
32        }
33
34        return dp[n][2];
35    }
36};