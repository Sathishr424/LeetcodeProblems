// Last updated: 12/20/2025, 11:55:01 AM
1class Solution {
2public:
3    bool isSorted(vector<string>& strs, int col, int n) {
4        int prev = -1;
5        for (int i=0; i<n; i++) {
6            int curr = (int) strs[i][col];
7            if (curr < prev) return false;
8            prev = curr;
9        }
10        return true;
11    }
12
13    int minDeletionSize(vector<string>& strs) {
14        int deleted = 0;
15        int n = strs.size();
16        int cols = strs[0].length();
17
18        for (int c=0; c<cols; c++) {
19            if (!isSorted(strs, c, n)) {
20                deleted++;
21            }
22        }
23
24        return deleted;
25    }
26};