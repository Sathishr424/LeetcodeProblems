# Last updated: 9/8/2025, 7:11:38 am
class Solution:
    def kthSmallestPrimeFraction(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        l = 0
        r = 1
        
        while l < r:
            mid = (l + r) / 2
            
            count = 0
            nume = 0
            deno = 0
            diff = 0
            j = 1
            # [1,13,17,59]
            for i in range(n-1):
                while j < n and nums[j] * mid <= nums[i]:
                    j += 1
                
                count += n - j
            
                if j == n: break

                f = nums[i] / nums[j]
                if f > diff:
                    diff = f
                    nume = i
                    deno = j

            if count == k:
                return [nums[nume], nums[deno]]
                r = mid
            elif count < k:
                l = mid
            else:
                r = mid

        return []