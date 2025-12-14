// Last updated: 12/14/2025, 2:01:27 PM
1const int N = 1e5 + 1;
2int dp[N][3];
3
4class Solution {
5public:
6    int numberOfWays(string corridor) {
7        int mod = 1e9 + 7;
8        int n = corridor.length();
9        for (int i=0; i<=n; i++) {
10            memset(dp[i], 0, sizeof(dp[0]));
11        }
12        dp[0][0] = 1;
13
14        for (int i=0; i<n; i++) {
15            char c = corridor[i];
16            for (int s=0; s<=2; s++) {
17                if (c == 'S') {
18                    if (s == 2) {
19                        dp[i + 1][1] += dp[i][s];
20                        dp[i + 1][1] %= mod;
21                    } else {
22                        dp[i + 1][s + 1] += dp[i][s];
23                        dp[i + 1][s + 1] %= mod;
24                    }
25                } else {
26                    if (s == 2) {
27                        dp[i + 1][0] += dp[i][s];
28                        dp[i + 1][0] %= mod;
29                    }
30                    dp[i + 1][s] += dp[i][s];
31                    dp[i + 1][s] %= mod;
32                }
33            }
34        }
35
36        return dp[n][2];
37    }
38};