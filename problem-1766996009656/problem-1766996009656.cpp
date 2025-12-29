// Last updated: 12/29/2025, 1:43:29 PM
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
28        auto it = memo.find(key);
29        if (it != memo.end()) return it->second;
30
31        int left = (prevMask / pows[index]) % 6;
32        int right = (prevMask / pows[index - 1]) % 6;
33        int mask = left * 6 + right;
34        for (int c: canUse[mask]) {
35            if (dfs(index - 1, row, prevMask, currMask * 6 + c, canUse, memo)) {
36                return memo[key] = true;
37            }
38        }
39        return memo[key] = false;
40    }
41
42    bool pyramidTransition(string bottom, vector<string>& allowed) {
43        int n = bottom.length();
44
45        unordered_map<int, vector<int>> canUse;
46
47        for (string st: allowed) {
48            int left = charToInt(st[0]);
49            int right = charToInt(st[1]);
50            int top = charToInt(st[2]);
51
52            int mask = left * 6 + right;
53            canUse[mask].push_back(top);
54        }
55
56        int prevMask = 0;
57        for (char c: bottom) {
58            int val = charToInt(c);
59            prevMask = prevMask * 6 + val;
60        }
61
62        unordered_map<long long, bool> memo;
63
64        return dfs(n - 1, n - 1, prevMask, 0, canUse, memo);
65    }
66};