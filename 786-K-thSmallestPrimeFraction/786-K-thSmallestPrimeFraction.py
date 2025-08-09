# Last updated: 9/8/2025, 7:06:40 am
class Solution:
    def kthSmallestPrimeFraction(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        l = 0
        r = 1
        add = 0.0000001
        numerator = 0
        denominator = 0
        
        while l < r:
            mid = (l + r) / 2
            
            count = 0
            nume = 0
            deno = 0
            diff = 0
            # [1,13,17,59]
            for i in range(n-1):
                j = n-1
                while j > i and nums[j] * mid >= nums[i]:
                    j -= 1
                
                j += 1
                if j == n: continue
                count += n - j
                if nums[i] / nums[j] > diff:
                    diff = nums[i] / nums[j]
                    nume = i
                    deno = j

            # print((l, mid, r), count, (nume, deno))
            if count >= k:
                numerator = nume
                denominator = deno
                r = mid - add
            else:
                l = mid + add

        return [nums[numerator], nums[denominator]]