// Last updated: 12/28/2025, 10:06:25 AM
1class Solution {
2public:
3    int countNegatives(vector<vector<int>>& grid) {
4        int m = grid.size();
5        int n = grid[0].size();
6
7        int ans = 0;
8        int j = n;
9        for (int i=0; i<m; i++) {
10            while (j - 1 >= 0 && grid[i][j - 1] < 0) {
11                j--;
12            }
13            ans += n - j;
14        }
15        return ans;
16    }
17};