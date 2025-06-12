# Last updated: 12/6/2025, 5:40:25 am
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(reverse=True, key=lambda e: e[1] - e[0])
        # print(tasks)
        ret = tasks[0][1]
        tot = tasks[0][1]
        for t in tasks:
            # print(t, tot, t[1] - ret if t[1] > ret else 0, ret + (t[1] - ret if t[1] > ret else 0) - t[0])
            tot += t[1] - ret if t[1] > ret else 0
            ret += t[1] - ret if t[1] > ret else 0
            ret -= t[0]
        return tot