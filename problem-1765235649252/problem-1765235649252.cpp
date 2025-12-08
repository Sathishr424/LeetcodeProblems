// Last updated: 12/9/2025, 4:44:09 AM
1class Solution {
2public:
3    int dfs(vector<vector<int>>& grid, int n, int row, int col, int vis_count) {
4        for (int i=-2; i<=2; i++) {
5            if (i == 0) continue;
6            for (int j=-2; j<=2; j++) {
7                if (j == 0) continue;
8
9                int i2 = row + i;
10                int j2 = col + j;
11
12                if (i2 >= 0 && i2 < n && j2 >= 0 && j2 < n && grid[i2][j2] == vis_count) {
13                    return dfs(grid, n, i2, j2, vis_count + 1);
14                }
15            }
16        }
17        return vis_count;
18    }
19    
20    bool checkValidGrid(vector<vector<int>>& grid) {
21        int n = grid.size();
22
23        return grid[0][0] == 0 && dfs(grid, n, 0, 0, 1) == n * n;
24    }
25};