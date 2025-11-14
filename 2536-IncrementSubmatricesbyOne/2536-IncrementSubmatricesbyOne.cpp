// Last updated: 14/11/2025, 4:30:36 pm
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        // Use a vector for the difference array (size N+1 to handle boundary conditions)
        vector<vector<int>> diff(n + 1, vector<int>(n + 1, 0));
        vector<vector<int>> ret(n, vector<int>(n, 0));
        
        for (const auto& query : queries) {
            int i1 = query[0];
            int j1 = query[1];
            int i2 = query[2];
            int j2 = query[3];

            diff[i1][j1] += 1;
            diff[i1][j2 + 1] -= 1;
            diff[i2 + 1][j1] -= 1;
            diff[i2 + 1][j2 + 1] += 1;
        }

        // Calculate the 2D prefix sum efficiently in one loop
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // Combine top and left values
                diff[i][j] += (i > 0 ? diff[i - 1][j] : 0) + (j > 0 ? diff[i][j - 1] : 0) - (i > 0 && j > 0 ? diff[i - 1][j - 1] : 0);
                ret[i][j] = diff[i][j];
            }
        }

        return ret;
    }
};
