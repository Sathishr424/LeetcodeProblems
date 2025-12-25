// Last updated: 12/25/2025, 7:09:29 PM
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

int inf = INT_MAX;
class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        k = min(k, 402);

        int dp[m][n][k + 1];

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int l = 0; l <= k; ++l) {
                    dp[i][j][l] = -inf;
                }
            }
        }

        dp[0][0][k] = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int rem = 0; rem <= k; rem++) {

                    for (int i2=0; i2<=1; i2++) {
                        for (int j2=0; j2<=1; j2++) {
                            if (i2 == j2) continue;
                            int i3 = i2 + i;
                            int j3 = j2 + j;
                            if (i3 < m && j3 < n && (grid[i3][j3] == 0 || rem >= 1)) {
                                int new_rem = rem - (grid[i3][j3] == 0 ? 0 : 1);
                                // cout << i3 << " " << j3 << " " << rem << endl;
                                dp[i3][j3][new_rem] = max(dp[i3][j3][new_rem], dp[i][j][rem] + grid[i3][j3]);
                                // cout << "ANS: " << dp[i][j][rem] << " " << dp[i3][j3][new_rem] << endl;
                            }
                        }
                    }

                }
            }
        }
        
        int ans = -1;
        for (int rem=0; rem<=k; rem++) {
            ans = max(ans, dp[m - 1][n - 1][rem]);
        }
        return ans;
    }
};