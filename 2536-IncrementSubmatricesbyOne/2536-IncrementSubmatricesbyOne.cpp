// Last updated: 14/11/2025, 4:30:45 pm
int diff[501][501];
class Solution {
public:
    vector<vector<int>> rangeAddQueries(int n, vector<vector<int>>& queries) {
        int q = queries.size();
        vector<vector<int>> ret(n, vector<int>(n, 0));
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                diff[i][j] = 0;
            }
        }

        for (int i=0; i<q; i++) {
            int i1 = queries[i][0];
            int j1 = queries[i][1];
            int i2 = queries[i][2];
            int j2 = queries[i][3];

            diff[i1][j1] += 1;
            diff[i1][j2 + 1] -= 1;
            diff[i2 + 1][j1] -= 1;
            diff[i2 + 1][j2 + 1] += 1;
        }

        for (int i=0; i<n; i++) {
            int curr=0;
            for (int j=0; j<n; j++) {
                curr += diff[i][j];
                ret[i][j] += curr;
            }
        }

        for (int j=0; j<n; j++) {
            int curr=0;
            for (int i=0; i<n; i++) {
                curr += ret[i][j];
                ret[i][j] = curr;
            }
        }

        return ret;
    }
};