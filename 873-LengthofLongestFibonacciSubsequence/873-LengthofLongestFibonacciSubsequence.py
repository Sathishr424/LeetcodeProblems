# Last updated: 15/5/2025, 1:42:04 am
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        def process(curr, prev):
            num = curr - prev
            if prev > num and num in added:
                return process(prev, arr[added[num]]) + 1
            return 0
        
        ret = 0
        added = {}
        for i in range(n):
            for j in range(i+1, n):
                curr = arr[j]
                prev = arr[i]
                ans = process(curr, prev)
                if ans > 0:
                    ret = max(ret, ans + 2)
                        
            added[arr[i]] = i
        
        return ret
