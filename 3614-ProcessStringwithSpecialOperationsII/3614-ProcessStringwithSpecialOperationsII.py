# Last updated: 6/17/2026, 5:38:31 PM
1class Solution:
2    def processStr(self, s: str, k: int) -> str:
3        n = len(s)
4
5        cnt = 0
6        chars = set()
7        for char in s:
8            if char == "*":
9                cnt = max(0, cnt - 1)
10            elif char == '%':
11                pass
12            elif char == '#':
13                cnt *= 2
14            else:
15                chars.add(char)
16                cnt += 1    
17        
18        # print(cnt)
19        if k >= cnt: return '.'
20        # print(list(chars))
21        s = s[::-1]
22
23        for a in chars:
24            pos = k
25            length = cnt
26            for char in s:
27                if char == "*":
28                    length += 1
29                elif char == '%':
30                    pos = length - pos - 1
31                elif char == '#':
32                    half = length // 2
33                    if pos >= half:
34                        pos -= half
35                    length = half
36                else:
37                    if pos == length - 1: 
38                        if char == a: return a
39                        break
40                    length -= 1
41                # print(a, char, pos, length)
42        
43        return '.'