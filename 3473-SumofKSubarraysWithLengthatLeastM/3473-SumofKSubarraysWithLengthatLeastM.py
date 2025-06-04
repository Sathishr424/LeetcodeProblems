# Last updated: 4/6/2025, 10:31:38 pm
class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        inf = float('inf')
        
        @cache
        def rec(index, k, expand):
            if k == 0 and (not expand or index == n): return 0

            ans = -inf
            if index+1 <= n-(k*m):
                ans = rec(index+1, k, False)
            
            if expand and index+1 <= n-(k*m):
                ans = max(ans, rec(index+1, k, True) + nums[index])
            if k > 0:
                t = prefix[index+m] - prefix[index]

                ans = max(ans, rec(index+m, k-1, True) + t)
            
            return ans
        
        ans = rec(0, k, False)

        return ans