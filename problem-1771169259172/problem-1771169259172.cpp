// Last updated: 2/15/2026, 8:57:39 PM
1#include <cstring>
2#include <iostream>
3#include <unordered_map>
4#include <vector>
5
6using namespace std;
7
8int getMax(string& s, int l, int r, int& n) {
9  while (l >= 0 && r < n) {
10    if (s[l] != s[r]) return max(0, r-l-1);
11    l--;
12    r++;
13  }
14  return max(0, r - l - 1);
15}
16
17class Solution {
18public:
19  int almostPalindromic(string s) {
20    int n = s.length();
21    int best = 2;
22
23    for (int i = 0; i < n; i++) {
24      int l = i - 1;
25      int r = i + 1;
26      bool wrong = false;
27
28      while (l >= 0 && r < n) {
29        if (s[l] != s[r]) {
30          best = max(best, max(getMax(s, l-1, r, n), getMax(s, l, r+1, n)));
31          l = 0;
32          r = 0;
33        }
34        l--;
35        r++;
36      }
37      l = max(0, l);
38      r = min(n-1, r);
39
40      best = max(best, r - l + 1);
41
42      l = i;
43      r = i+1;
44      wrong = false;
45
46      while (l >= 0 && r < n) {
47        if (s[l] != s[r]) {
48          best = max(best, max(getMax(s, l-1, r, n), getMax(s, l, r+1, n)));
49          l = 0;
50          r = 0;
51        }
52        l--;
53        r++;
54      }
55
56      l = max(0, l);
57      r = min(n-1, r);
58
59      best = max(best, r - l + 1);
60    }
61
62    return best;
63  }
64};
65