// Last updated: 12/30/2025, 2:41:08 PM
1class Solution {
2public:
3    vector<pair<int, int>> dirs = {{1, 0}, {0, 1}};
4    bool isMagicSquare(vector<vector<int>>& grid, int i, int j) {
5        int mask = 0;
6        for (int i2=i; i2<i+3; i2++) {
7            for (int j2=j; j2<j+3; j2++) {
8                int cell = grid[i2][j2];
9                if (cell < 1 || cell > 9 || (mask & (1 << cell)) != 0) return false;
10                mask |= 1 << cell;
11            }
12        }
13
14        int prev = -1;
15        for (int i2=i; i2<i+3; i2++) {
16            int sum = 0;
17            for (int k=0; k<3; k++) {
18                sum += grid[i2][j + k];
19            }
20            if (prev != -1 && sum != prev) return false;
21            prev = sum;
22        }
23
24        for (int j2=j; j2<j+3; j2++) {
25            int sum = 0;
26            for (int k=0; k<3; k++) {
27                sum += grid[i + k][j2];
28            }
29            if (sum != prev) return false;
30        }
31
32        int i2 = i;
33        int j2 = j;
34        int sum = 0;
35        for (int k=0; k<3; k++) {
36            sum += grid[i2][j2];
37            i2 += 1;
38            j2 += 1;
39        }
40        if (sum != prev) return false;
41
42        i2 = i + 2;
43        j2 = j;
44        sum = 0;
45        for (int k=0; k<3; k++) {
46            sum += grid[i2][j2];
47            i2 -= 1;
48            j2 += 1;
49        }
50        return sum == prev;
51    }
52
53    int numMagicSquaresInside(vector<vector<int>>& grid) {
54        int m = grid.size();
55        int n = grid[0].size();
56        int cnt = 0;
57
58        for (int i=0; i<m-2; i++) {
59            for (int j=0; j<n-2; j++) {
60                if (isMagicSquare(grid, i, j)) {
61                    cnt++;
62                }
63            }
64        }
65        return cnt;
66    }
67};