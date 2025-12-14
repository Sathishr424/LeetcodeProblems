// Last updated: 12/14/2025, 2:04:23 PM
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
17            for (int s=0; s<=2; s++) {
18                if (corridor[i] == 'S') {
19                    if (s == 2) {
20                        dp[i + 1][1] += dp[i][s];
21                        dp[i + 1][1] %= mod;
22                    } else {
23                        dp[i + 1][s + 1] += dp[i][s];
24                        dp[i + 1][s + 1] %= mod;
25                    }
26                } else {
27                    if (s == 2) {
28                        dp[i + 1][0] += dp[i][s];
29                        dp[i + 1][0] %= mod;
30                    }
31                    dp[i + 1][s] += dp[i][s];
32                    dp[i + 1][s] %= mod;
33                }
34            }
35        }
36
37        return dp[n][2];
38    }
39};