# Last updated: 1/18/2026, 7:41:23 PM
1class Solution:
2    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
3        n = len(costs)
4        budget -= 1
5
6        best = 0
7        new_arr = []
8        for i in range(n):
9            if costs[i] <= budget:
10                best = max(best, capacity[i])
11            new_arr.append((costs[i], i))
12
13        new_arr.sort()
14        # print(new_arr)
15
16        max_cap = 0
17        prefix = [0]
18        vals = []
19        for i in range(n):
20            cap = capacity[new_arr[i][1]]
21            max_cap = max(cap, max_cap)
22            rem = budget - new_arr[i][0]
23
24            if rem > 0:
25                index = bisect_right(new_arr, (rem, inf), hi=i)
26                best = max(best, cap + prefix[index])
27            
28            prefix.append(max_cap)
29
30        return best
31                
32