// Last updated: 12/29/2025, 1:32:05 PM
1int pows[6];
2
3struct Init {
4    Init() {
5        pows[0] = 1;
6        for (int i=1; i<6; i++) {
7            pows[i] = pows[i - 1] * 6;
8        }
9    }
10} initiate;
11
12class Solution {
13public:
14    int charToInt(char c) {
15        return c - 'A';
16    }
17
18    bool dfs(int index, int row, int prevMask, int currMask, unordered_map<int, vector<int>> &canUse) {
19        if (row == 0) return true;
20        if (index == 0) return dfs(row - 1, row - 1, currMask, 0, canUse);
21        // cout << index << " " << row << " " << prevMask << " " << currMask << endl;
22
23        int left = (prevMask / pows[index]) % 6;
24        int right = (prevMask / pows[index - 1]) % 6;
25        int mask = left * 6 + right;
26        for (int c: canUse[mask]) {
27            if (dfs(index - 1, row, prevMask, currMask * 6 + c, canUse)) return true;
28        }
29        return false;
30    }
31
32    bool pyramidTransition(string bottom, vector<string>& allowed) {
33        int n = bottom.length();
34
35        unordered_map<int, vector<int>> canUse;
36
37        for (string st: allowed) {
38            int left = charToInt(st[0]);
39            int right = charToInt(st[1]);
40            int top = charToInt(st[2]);
41
42            int mask = left * 6 + right;
43            canUse[mask].push_back(top);
44        }
45
46        int prevMask = 0;
47        for (char c: bottom) {
48            int val = charToInt(c);
49            prevMask = prevMask * 6 + val;
50        }
51
52        return dfs(n - 1, n - 1, prevMask, 0, canUse);
53    }
54};