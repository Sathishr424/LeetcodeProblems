# Last updated: 1/4/2026, 3:36:26 PM
1class Solution:
2    def wordSquares(self, words: List[str]) -> List[List[str]]:
3        n = len(words)
4        # 0[0] == 1[0] && 0[3] == 2[0] && 1[3] == 3[0] && 2[3] == 3[3]
5
6        ret = []
7        for i in range(n):
8            top = words[i]
9            for j in range(n):
10                bottom = words[j]
11                for k in range(n):
12                    if len(set([i, j, k])) != 3: continue
13                    left = words[k]
14                    if left[0] != top[0] or left[3] != bottom[0]: continue
15                    for l in range(n):
16                        if len(set([i, j, k, l])) != 4: continue
17                        right = words[l]
18                        if right[0] != top[3] or right[3] != bottom[3]: continue
19                        ret.append([top, left, right, bottom])
20            
21
22        return sorted(ret)