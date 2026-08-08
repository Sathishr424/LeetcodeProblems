# Last updated: 8/8/2026, 3:37:17 PM
1class Solution:
2    def validSequence(self, word1: str, word2: str) -> List[int]:
3        m = len(word1)
4        n = len(word2)
5
6        if n > m: return []
7
8        index = n-1
9        suffix = [-1] * m
10        for i in range(m-1, -1, -1):
11            if index >= 0 and word1[i] == word2[index]:
12                index -= 1
13            suffix[i] = index + 1
14
15        index = 0
16        left = []
17        for i in range(m-1):
18            if index < n and word1[i] == word2[index]:
19                left.append(i)
20                index += 1
21            elif len(left) < n and suffix[i+1] <= index + 1:
22                left.append(i)
23                r_index = index + 1
24                for j in range(i+1, m):
25                    if r_index < n and word1[j] == word2[r_index]:
26                        left.append(j)
27                        r_index += 1
28                return left
29        
30        if len(left) == n: return left
31        elif len(left) and len(left) == n-1: 
32            left.append(m-1)
33            return left
34        return []