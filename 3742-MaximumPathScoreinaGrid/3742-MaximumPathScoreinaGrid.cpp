// Last updated: 10/11/2025, 7:58:53 pm
#include <iostream>
#include <vector>

using namespace std;

int inf = INT_MAX;
class Solution {
public:
    int DIR[2][2];
    Solution() : DIR{{1, 0}, {0, 1}} {

    }
    int rec(int i, int j, int m, int n, int rem, vector<vector<int>>& grid, vector<vector<vector<int>>>& memo) {
        if (rem < 0) return -inf;
        if (i == m - 1 && j == n - 1) return 0;
        if (memo[i][j][rem] != -1) return memo[i][j][rem];

        int ans = -inf;
        for (int d = 0; d < 2; d++) {
            int i2 = i + DIR[d][0];
            int j2 = j + DIR[d][1];

            if (i2 >= 0 && i2 < m && j2 >= 0 && j2 < n && (grid[i2][j2] == 0 || rem >= 1)) {
                ans = max( ans, rec(i2, j2, m, n, rem - (grid[i2][j2] == 0 ? 0 : 1), grid, memo) + grid[i2][j2] );
            }
        }
        memo[i][j][rem] = ans;
        return ans;
    }

    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<vector<int>>> memo(
            m, vector<vector<int>>(n, vector<int>(k + 1, -1))
        );
        int ans = rec(0, 0, m, n, k, grid, memo);

        return ans <= -(inf - 1000) ? -1 : ans;
    }
};