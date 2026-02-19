// Last updated: 2/19/2026, 10:22:48 PM
1#include <iostream>
2
3using namespace std;
4
5class Solution {
6public:
7  int findTheLongestBalancedSubstring(string s) {
8    int n = s.length();
9
10    int best = 0;
11    int prev = 0;
12    int cnt = 1;
13    char curr = s[0];
14    for (int i=1; i<n; i++) {
15      if (s[i] == curr) cnt++;
16      else {
17        if (curr == '1') best = max(best, min(cnt, prev) * 2);
18        prev = cnt;
19        cnt = 1;
20        curr = s[i];
21      }
22    }
23
24    if (curr == '1') best = max(best, min(cnt, prev) * 2);
25
26    return best;
27  }
28};
29