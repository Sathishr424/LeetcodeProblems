// Last updated: 12/29/2025, 1:40:44 PM
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
18    bool dfs(int index, int row, int prevMask, int currMask, unordered_map<int, vector<int>> &canUse, unordered_map<long long, bool> &memo) {
19        if (row == 0) return true;
20        if (index == 0) return dfs(row - 1, row - 1, currMask, 0, canUse, memo);
21
22        long long key =
23            ((long long)index << 48) |
24            ((long long)row << 40) |
25            ((long long)prevMask << 20) |
26            currMask;
27        
28        if (memo.count(key)) return memo[key];
29
30        int left = (prevMask / pows[index]) % 6;
31        int right = (prevMask / pows[index - 1]) % 6;
32        int mask = left * 6 + right;
33        for (int c: canUse[mask]) {
34            if (dfs(index - 1, row, prevMask, currMask * 6 + c, canUse, memo)) {
35                return memo[key] = true;
36            }
37        }
38        return memo[key] = false;
39    }
40
41    bool pyramidTransition(string bottom, vector<string>& allowed) {
42        int n = bottom.length();
43
44        unordered_map<int, vector<int>> canUse;
45
46        for (string st: allowed) {
47            int left = charToInt(st[0]);
48            int right = charToInt(st[1]);
49            int top = charToInt(st[2]);
50
51            int mask = left * 6 + right;
52            canUse[mask].push_back(top);
53        }
54
55        int prevMask = 0;
56        for (char c: bottom) {
57            int val = charToInt(c);
58            prevMask = prevMask * 6 + val;
59        }
60
61        unordered_map<long long, bool> memo;
62
63        return dfs(n - 1, n - 1, prevMask, 0, canUse, memo);
64    }
65};