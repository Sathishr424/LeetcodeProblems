// Last updated: 11/11/2025, 2:11:17 pm
#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

struct b_size{
    int ones = 0;
    int zeroes = 0;

    b_size() {

    }
};

class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int N = strs.size();

        vector<b_size> sizes(N);
        for (int i = 0; i < N; i++) {
            int one = 0;
            int zero = 0;

            for (int j = 0; j < strs[i].length(); j++) {
                if (strs[i][j] == '0') zero++;
                else one++;
            }

            sizes[i].ones = one;
            sizes[i].zeroes = zero;
        }
        int neg_inf = INT_MIN;

        int dp[N + 1][m + 1][n + 1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    dp[i][j][k] = neg_inf;
                }
            }
        }
        dp[0][m][n] = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    int ones = sizes[i].ones;
                    int zeroes = sizes[i].zeroes;

                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k]);
                    if (j >= zeroes && k >= ones) {
                        dp[i + 1][j - zeroes][k - ones] = max(dp[i + 1][j - zeroes][k - ones], dp[i][j][k] + 1);
                    }
                }
            }
        }

        int ans = 0;
        for (int j = 0; j <= m; j++) {
            for (int k = 0; k <= n; k++) {
                ans = max(ans, dp[N][j][k]);
            }
        }

        return ans;
    }
};
