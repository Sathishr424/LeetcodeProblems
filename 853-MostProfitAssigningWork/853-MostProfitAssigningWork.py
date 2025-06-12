# Last updated: 12/6/2025, 5:46:15 am
class Solution:
    def maxProfitAssignment(self, diff: List[int], profit: List[int], worker: List[int]) -> int:
        arr = []

        for i, p in enumerate(profit):
            arr.append((p, i))

        arr.sort(key=lambda x: x[0], reverse=True)

        worker.sort()
        index = len(worker)-1
        ret = 0
        for p, i in arr:
            while index >= 0 and worker[index] >= diff[i]:
                index -= 1
                ret += p
            if index == -1: return ret
        return ret