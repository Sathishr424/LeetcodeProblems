// Last updated: 28/9/2025, 12:17:47 pm
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const int MOD = 1e9 + 7;
        int m = r - l + 1;

        // dp[i][j][k] = number of ways at index i, value j, state k
        vector<vector<array<long long, 2>>> dp(n + 1, vector<array<long long, 2>>(m, {0, 0}));

        long long prev = 0;
        for (int i = 0; i < m; i++) {
            if (i + 1 < m) {
                dp[0][i][1] = 1;
            }
            if (i > 0) {
                prev += 1;
                dp[0][i][0] = 1;
            }
        }

        long long cnt = 0;
        for (int i = 0; i < n; i++) {
            long long new_prev = 0;
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < 2; k++) {
                    dp[i][j][k] %= MOD;
                    if (k == 1) {
                        cnt += dp[i][j][k];
                        if (j + 1 < m) {
                            dp[i + 1][j + 1][0] += cnt;
                            new_prev += dp[i + 1][j + 1][0];
                        }
                    } else {
                        prev -= dp[i][j][k];
                        dp[i + 1][j][1] += prev;
                    }
                }
            }
            prev = new_prev;
            cnt = 0;
        }

        return (dp[n][0][1] + dp[n][m - 1][0]) % MOD;
    }
};
