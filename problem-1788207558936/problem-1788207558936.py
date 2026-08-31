# Last updated: 9/1/2026, 1:49:18 AM
1class Solution:
2    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
3        n = len(tasks)
4
5        prefix = [0]
6        for t in tasks:
7            prefix.append(prefix[-1] + t)
8        prefix.append(prefix[-1])
9
10        def isGood(shift, index, rem):
11            return shift + rem >= prefix[index]
12
13        ret = []
14        prev = 0
15        rem = 0
16        for shift in shifts:
17            l = prev
18            r = n
19
20            while l < r:
21                mid = (l + r + 1) // 2
22
23                if isGood(shift, mid, rem):
24                    l = mid
25                else:
26                    r = mid - 1
27
28            rem = max(0, prefix[l + 1] - (prefix[l + 1] - (shift + rem)))
29            if l == n:
30                rem = 0
31            prev = l % n
32            ret.append(n - l)
33
34        return ret