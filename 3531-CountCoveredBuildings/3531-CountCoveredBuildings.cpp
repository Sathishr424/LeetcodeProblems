// Last updated: 12/11/2025, 11:29:09 AM
1class Solution {
2public:
3    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
4        unordered_map<int, int> v_min, v_max, h_min, h_max;
5
6        for (auto cord: buildings) {
7            int x = cord[0];
8            int y = cord[1];
9
10            h_min[x] = min(h_min[x] == 0 ? y : h_min[x], y);
11            h_max[x] = max(h_max[x], y);
12
13            v_min[y] = min(v_min[y] == 0 ? x : v_min[y], x);
14            v_max[y] = max(v_max[y], x);
15            
16        }
17
18        int count = 0;
19        for (auto cord: buildings) {
20            int x = cord[0];
21            int y = cord[1];
22
23            if (h_min[x] < y && h_max[x] > y && v_min[y] < x && v_max[y] > x) {
24                count++;
25            }
26        }
27
28        return count;
29    }
30};