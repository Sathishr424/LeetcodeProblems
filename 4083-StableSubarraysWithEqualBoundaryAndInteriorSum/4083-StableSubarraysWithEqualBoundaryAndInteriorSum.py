# Last updated: 12/25/2025, 7:08:23 PM
class Solution:
    def countStableSubarrays(self, cap: List[int]) -> int:
        n = len(cap)

        indexes = defaultdict(list)

        for i in range(n):
            indexes[cap[i]].append(i)

        sl = SortedList()
        s = 0
        prefix = []
        for i in range(2):
            s += cap[i]
            prefix.append(s)

        stable = 0
        for i in range(2, n):
            sl.add((prefix[i-2], cap[i-2]))
            num = cap[i]
            need = s - num

            l = sl.bisect_left((need, num))
            r = sl.bisect_right((need, num))
            # print(i, num, (l, r), sl, s)

            stable += r - l
            
            s += cap[i]
            prefix.append(s)

        return stable