# Last updated: 15/5/2025, 1:39:12 am
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        @cache
        def process(curr, prev):
            num = curr - prev
            cnt = 2
            while prev > num and num in added:
                cnt += 1
                curr = prev
                prev = arr[added[num]]
                num = curr - prev
            return cnt
        
        ret = 0
        added = {}
        for i in range(n):
            for j in range(i+1, n):
                curr = arr[j]
                prev = arr[i]
                ans = process(curr, prev)
                if ans > 2:
                    ret = max(ret, ans)
                        
            added[arr[i]] = i
        
        return ret
