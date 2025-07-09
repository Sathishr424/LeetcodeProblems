# Last updated: 9/7/2025, 11:10:04 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        prefix = [startTime[0] - 0]
        for i in range(1, n):
            prefix.append(startTime[i] - endTime[i-1])
        prefix.append(eventTime - endTime[n-1])

        k += 1
        curr = sum(prefix[:k])
        ret = curr
        for i in range(k, n + 1):
            curr = curr - prefix[i - k] + prefix[i]
            ret = cmax(curr, ret)
        
        return ret