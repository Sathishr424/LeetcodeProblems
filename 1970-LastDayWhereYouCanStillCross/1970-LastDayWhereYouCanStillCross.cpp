// Last updated: 12/31/2025, 1:24:30 PM
1class UnionFind {
2public:
3    vector<int> parents;
4    vector<int> sizes;
5
6    UnionFind(int n) {
7        parents.resize(n);
8        sizes.resize(n, 1);
9
10        for (int i=0; i<n; i++) parents[i] = i;
11    }
12
13    int find(int x) {
14        if (parents[x] != x) {
15            parents[x] = find(parents[x]);
16        }
17        return parents[x];
18    }
19
20    bool join(int x, int y) {
21        x = find(x);
22        y = find(y);
23
24        if (x == y) return false;
25
26        if (sizes[x] < sizes[y]) {
27            x ^= y;
28            y ^= x;
29            x ^= y;
30        }
31
32        parents[y] = x;
33        sizes[x] += sizes[y];
34        return true;
35    }
36};
37
38
39class Solution {
40public:
41    vector<pair<int, int>> dirs = {{1, 0}, {0, 1}};
42    bool isGood(int& n, int& day, int& row, int& col, vector<vector<int>>& cells) {
43        UnionFind uf(n);
44        vector<int> grid(n);
45
46        for (int i=0; i<day; i++) {
47            int pos = (cells[i][0] - 1) * col + (cells[i][1] - 1);
48            grid[pos] = 1;
49        }
50
51        for (int i=0; i<row; i++) {
52            for (int j=0; j<col; j++) {
53                int pos = i * col + j;
54                if (grid[pos] == 1) continue;
55                for (auto& d: dirs) {
56                    int i2 = i + d.first;
57                    int j2 = j + d.second;
58                    if (i2 >= 0 && i2 < row && j2 >= 0 && j2 < col && grid[i2 * col + j2] != 1) {
59                        uf.join(pos, i2 * col + j2);
60                    }
61                }
62            }
63        }
64
65        int last = (row  - 1) * col;
66        for (int i=1; i<col; i++) {
67            uf.join(i, i-1);
68            uf.join(last + i, last + i - 1);
69        }
70        return uf.find(0) == uf.find(n-1);
71    }
72
73    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
74        int l = 0;
75        int r = cells.size();
76        int n = row * col;
77
78        while (l < r) {
79            int mid = (l + r + 1) / 2;
80
81            if (isGood(n, mid, row, col, cells)) {
82                l = mid;
83            } else {
84                r = mid - 1;
85            }
86        }
87
88        return l;
89    }
90};