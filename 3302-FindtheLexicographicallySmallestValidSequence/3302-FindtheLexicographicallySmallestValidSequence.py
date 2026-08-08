# Last updated: 8/8/2026, 3:18:04 PM
1class Solution:
2    def validSequence(self, word1: str, word2: str) -> List[int]:
3        m = len(word1)
4        n = len(word2)
5
6        if n > m: return []
7
8        index = 0
9        prefix = [-1] * m
10        for i in range(m):
11            if index < n and word1[i] == word2[index]:
12                index += 1
13            prefix[i] = index - 1
14
15        index = n-1
16        suffix = [-1] * m
17        for i in range(m-1, -1, -1):
18            if index >= 0 and word1[i] == word2[index]:
19                index -= 1
20            suffix[i] = index + 1
21
22        index = 0
23        left = []
24        # print(suffix)
25        for i in range(m-1):
26            if index < n and word1[i] == word2[index]:
27                left.append(i)
28                index += 1
29            elif len(left) < n and suffix[i+1] <= index + 1:
30                left.append(i)
31                r_index = index + 1
32                for j in range(i+1, m):
33                    if r_index < n and word1[j] == word2[r_index]:
34                        left.append(j)
35                        r_index += 1
36                return left
37        
38        if len(left) == n: return left
39        elif len(left) == n-1 and left and left[-1] != m-1: return left + [m-1]
40        return []