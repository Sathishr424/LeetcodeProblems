# Last updated: 8/8/2026, 3:00:11 PM
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
24        for i in range(m):
25            if index < n and word1[i] == word2[index]:
26                left.append(i)
27                index += 1
28            elif len(left) < n and suffix[i] <= index + 1 and i+1 < m and suffix[i+1] == suffix[i]:
29                left.append(i)
30                r_index = index + 1
31                for j in range(i+1, m):
32                    if r_index < n and word1[j] == word2[r_index]:
33                        left.append(j)
34                        r_index += 1
35                return left
36        
37        if len(left) == n: return left
38        elif len(left) == n-1 and left and left[-1] != m-1: return left + [m-1]
39        return []