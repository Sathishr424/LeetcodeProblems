# Last updated: 10/7/2025, 7:08:53 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        prefix = [startTime[0]]

        for i in range(1, n):
            prefix.append(startTime[i] - endTime[i-1])
        prefix.append(eventTime - endTime[-1])

        k = 2
        curr = sum(prefix[:k])
        ret = curr

        for i in range(k, n+1):
            curr = curr - prefix[i - k] + prefix[i]
            ret = cmax(ret, curr)
        
        left = [0] * (n + 1)
        left[0] = prefix[0]
        right = [0] * (n + 1)
        right[-1] = prefix[-1]

        for i in range(n-1, -1, -1):
            right[i] = cmax(right[i+1], prefix[i])
        for i in range(1, n+1):
            left[i] = cmax(left[i-1], prefix[i])

        for i in range(n):
            dur = endTime[i] - startTime[i]
            if (i != 0 and dur <= left[i-1]) or (i != n-1 and dur <= right[i+2]):
                ret = cmax(ret, dur + prefix[i] + prefix[i+1])

        return ret