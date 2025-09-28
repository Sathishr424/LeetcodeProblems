// Last updated: 28/9/2025, 12:32:55 pm
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        const int MOD = 1e9 + 7;
        int m = r - l + 1;

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
            long long newPrev = 0;
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < 2; k++) {
                    if (k == 1) {
                        cnt = (cnt + dp[i][j][k]) % MOD;
                        if (j + 1 < m) {
                            dp[i + 1][j + 1][0] = cnt;
                            newPrev = (newPrev + dp[i + 1][j + 1][0]) % MOD;
                        }
                    } else {
                        prev = (prev - dp[i][j][k] + MOD) % MOD;
                        dp[i + 1][j][1] = prev;
                    }
                }
            }
            prev = newPrev;
            cnt = 0;
        }

        return (int)((dp[n][0][1] + dp[n][m - 1][0]) % MOD);
    }
};
