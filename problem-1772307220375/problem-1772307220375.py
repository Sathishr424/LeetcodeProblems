# Last updated: 3/1/2026, 1:03:40 AM
1class Solution:
2    def mergeCharacters(self, s: str, k: int) -> str:
3        n = len(s)
4
5        stack = list(s)
6
7        change = True
8        while change:
9            change = False
10            for i in range(len(stack)):
11                for j in range(i+1, len(stack)):
12                    if stack[i] == stack[j] and (j - i) <= k:
13                        stack = stack[:j] + stack[j+1:]
14                        change = True
15                        break
16                if change: break
17
18        return ''.join(stack)
19                        
20                    
21        indexes = defaultdict(deque)
22        for i in range(n):
23            indexes[s[i]].append(i)
24
25        ret = ""
26        index = 0
27        for i in range(n):
28            c = s[i]
29            if indexes[c] and indexes[c][0] == i:
30                indexes[c].popleft()
31                ret += c
32                while indexes[c] and indexes[c][0] - i - index <= k:
33                    indexes[c].popleft()
34                    index += 1
35
36        return ret