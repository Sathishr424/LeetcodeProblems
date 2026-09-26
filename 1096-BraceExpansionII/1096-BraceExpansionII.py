# Last updated: 9/27/2026, 1:10:06 AM
1class Solution:
2    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
3        n = len(s)
4        keys = {}
5        for key, value in knowledge:
6            keys[key] = value
7
8        left = 0
9        ret = ""
10        for i in range(n):
11            if s[i] == '(':
12                ret += s[left:i]
13                left = i + 1
14            elif s[i] == ')':
15                key = s[left:i]
16                left = i + 1
17                if key in keys:
18                    ret += keys[key]
19                else:
20                    ret += "?"
21        if left != -1:
22            ret += s[left:]
23        return ret