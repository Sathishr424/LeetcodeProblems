# Last updated: 12/6/2025, 5:40:29 am
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)

        prefix = {}
        curr = 0
        ret = float('inf')
        for i in range(n):
            curr += nums[i]
            if curr == x: 
                ret = min(ret, i+1)
                break
            elif curr > x: break
            prefix[curr] = i

        curr = 0
        for i in range(n-1, -1, -1):
            curr += nums[i]
            if curr == x: 
                ret = min(ret, n-i)
                break
            elif curr > x: break
            elif x-curr in prefix and prefix[x-curr] < i:
                ret = min(ret, (n-i) + prefix[x-curr]+1)
        
        return ret if ret != float('inf') else -1
