# Last updated: 8/8/2026, 3:36:27 PM
1from typing import List
2
3class Solution:
4    def validSequence(self, word1: str, word2: str) -> List[int]:
5        m, n = len(word1), len(word2)
6        
7        # suff[i] stores the largest index in word1 such that word2[i:] 
8        # can be matched as an exact subsequence in word1[suff[i]:]
9        suff = [-1] * (n + 1)
10        suff[n] = m
11        
12        cur = m - 1
13        for i in range(n - 1, -1, -1):
14            while cur >= 0 and word1[cur] != word2[i]:
15                cur -= 1
16            suff[i] = cur
17            if cur >= 0:
18                cur -= 1
19                
20        ans = []
21        cur_w1 = 0
22        mismatch_used = False
23        
24        for i in range(n):
25            if not mismatch_used:
26                # If the remaining suffix can be matched with 0 mismatches,
27                # we can pick the smallest possible index `cur_w1` right away.
28                if cur_w1 + 1 <= suff[i + 1]:
29                    ans.append(cur_w1)
30                    if word1[cur_w1] != word2[i]:
31                        mismatch_used = True
32                    cur_w1 += 1
33                else:
34                    # Must find an exact match at or after cur_w1
35                    while cur_w1 < m and word1[cur_w1] != word2[i]:
36                        cur_w1 += 1
37                    if cur_w1 >= m:
38                        return []
39                    ans.append(cur_w1)
40                    cur_w1 += 1
41            else:
42                # Mismatch already used; must find exact match and verify remaining suffix is valid
43                while cur_w1 < m and word1[cur_w1] != word2[i]:
44                    cur_w1 += 1
45                if cur_w1 >= m or cur_w1 + 1 > suff[i + 1]:
46                    return []
47                ans.append(cur_w1)
48                cur_w1 += 1
49                
50        return ans