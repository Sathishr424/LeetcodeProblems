# Last updated: 9/7/2025, 11:08:38 am
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        merged = []
        for i in range(n):
            merged.append((startTime[i], endTime[i]))
        
        prefix = [merged[0][0] - 0]
        for i in range(1, n):
            prefix.append(merged[i][0] - merged[i-1][1])
        prefix.append(eventTime - merged[n-1][1])
        # print(merged)
        # print(prefix)
        k += 1
        curr = sum(prefix[:k])
        ret = curr
        for i in range(k, n + 1):
            curr -= prefix[i - k]
            curr += prefix[i]
            ret = max(curr, ret)
        
        return ret