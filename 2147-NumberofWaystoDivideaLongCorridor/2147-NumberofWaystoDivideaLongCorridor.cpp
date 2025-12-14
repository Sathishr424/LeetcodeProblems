// Last updated: 12/14/2025, 2:01:55 PM
1const int N = 1e5 + 1;
2int dp[N][3];
3
4class Solution {
5public:
6    int numberOfWays(string corridor) {
7        int mod = 1e9 + 7;
8        int n = corridor.length();
9        for (int i=0; i<=n; i++) {
10            dp[i][0] = 0;
11            dp[i][1] = 0;
12            dp[i][2] = 0;
13        }
14        dp[0][0] = 1;
15
16        for (int i=0; i<n; i++) {
17            char c = corridor[i];
18            for (int s=0; s<=2; s++) {
19                if (c == 'S') {
20                    if (s == 2) {
21                        dp[i + 1][1] += dp[i][s];
22                        dp[i + 1][1] %= mod;
23                    } else {
24                        dp[i + 1][s + 1] += dp[i][s];
25                        dp[i + 1][s + 1] %= mod;
26                    }
27                } else {
28                    if (s == 2) {
29                        dp[i + 1][0] += dp[i][s];
30                        dp[i + 1][0] %= mod;
31                    }
32                    dp[i + 1][s] += dp[i][s];
33                    dp[i + 1][s] %= mod;
34                }
35            }
36        }
37
38        return dp[n][2];
39    }
40};