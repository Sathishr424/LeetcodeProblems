// Last updated: 12/11/2025, 11:32:47 AM
1class Solution {
2public:
3    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
4        n++;
5        vector<int> h_min(n, INT_MAX);
6        vector<int> h_max(n, 0);
7        vector<int> v_min(n, INT_MAX);
8        vector<int> v_max(n, 0);
9
10        for (auto& cord: buildings) {
11            int x = cord[0];
12            int y = cord[1];
13
14            h_min[x] = min(h_min[x], y);
15            h_max[x] = max(h_max[x], y);
16
17            v_min[y] = min(v_min[y], x);
18            v_max[y] = max(v_max[y], x);
19            
20        }
21
22        int count = 0;
23        for (auto& cord: buildings) {
24            int x = cord[0];
25            int y = cord[1];
26
27            if (h_min[x] < y && h_max[x] > y && v_min[y] < x && v_max[y] > x) {
28                count++;
29            }
30        }
31
32        return count;
33    }
34};