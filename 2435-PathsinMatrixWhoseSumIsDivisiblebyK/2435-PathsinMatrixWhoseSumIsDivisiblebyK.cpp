// Last updated: 26/11/2025, 6:50:20 am
#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <unordered_map>
#include <unordered_set>

using namespace std;

const int mod = 1000000007;

class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        const int m = grid.size();
        const int n = grid[0].size();

        int dp[m + 1][n + 1][k];
        memset(dp, 0, sizeof(dp));
        dp[0][0][0] = 1;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                for (int rem=0; rem<k; rem++) {
                    int new_rem = (grid[i][j] + rem) % k;
                    dp[i + 1][j][new_rem] += dp[i][j][rem];
                    dp[i + 1][j][new_rem] %= mod;
                    dp[i][j + 1][new_rem] += dp[i][j][rem];
                    dp[i][j + 1][new_rem] %= mod;
                }
            }
        }

        return dp[m][n-1][0];
    }
};