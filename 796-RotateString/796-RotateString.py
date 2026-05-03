# Last updated: 5/3/2026, 5:44:18 PM
1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        n = len(s)
4        if n != len(goal): return False
5
6        for i in range(n):
7            for j in range(i, i + n):
8                index = j % n
9                if s[index] != goal[j-i]: break
10            else:
11                return True
12        
13        return False