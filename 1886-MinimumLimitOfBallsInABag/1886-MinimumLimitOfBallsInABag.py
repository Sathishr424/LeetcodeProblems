# Last updated: 12/6/2025, 5:39:56 am
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        ans = r
        while l <= r:
            mid = (l+r)//2

            operation = maxOperations

            for num in nums:
                operation -= ceil(num/mid)-1
                if operation < 0:
                    l = mid+1
                    break
            
            if operation >= 0:
                r = mid-1
                ans = min(ans, mid)
        
        return ans