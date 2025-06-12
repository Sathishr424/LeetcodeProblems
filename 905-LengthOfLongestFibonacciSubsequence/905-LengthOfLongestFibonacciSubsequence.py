# Last updated: 12/6/2025, 5:45:48 am
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        ret = 0
        added = {}
        for i in range(n):
            for j in range(i+1, n):
                curr = arr[j]
                prev = arr[i]
                num = curr - prev
                cnt = 2
                while prev > num and num in added:
                    cnt += 1
                    curr = prev
                    prev = arr[added[num]]
                    num = curr - prev
                if cnt > 2:
                    ret = max(ret, cnt)
                        
            added[arr[i]] = i
        
        return ret
