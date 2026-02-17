# Last updated: 2/17/2026, 11:15:28 PM
1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> List[str]:
3        ret = []
4        def add(st):
5            mins = 0
6            hour = 0
7            for i in range(len(st)):
8                if st[i] == '1':
9                    if i < 4: hour += 2**i
10                    else: mins += 2**(i-4)
11            if mins < 60 and hour < 12:
12                ret.append(f"{hour}:{mins if mins > 9 else f'0{mins}'}")
13
14        def rec(st, cnt):
15            if len(st) == 10:
16                if cnt == turnedOn: add(st)
17                return
18
19            rec(st+'0', cnt)
20            if cnt+1 <= turnedOn: rec(st+'1', cnt+1)
21
22        rec("", 0)
23        
24        return ret
25