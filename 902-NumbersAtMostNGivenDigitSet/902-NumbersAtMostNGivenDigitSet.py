# Last updated: 5/10/2025, 11:51:59 pm
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = [int(d) for d in digits]
        digits.sort()
        nums = [int(d) for d in str(n)]
        m = len(nums)

        @cache
        def rec(index, strict, add):
            if index == m: return 1

            ans = add
            if strict:
                for num in digits:
                    if num > nums[index]: break
                    ans += rec(index + 1, num == nums[index], add)
            else:
                for num in digits:
                    ans += rec(index + 1, 0, add)
            
            return ans

        ans = 0
        for num in digits:
            if num > nums[0]: break
            ans += rec(1, num == nums[0], 0)
        
        if 2 <= m:
            for num in digits:
                ans += rec(2, 0, 1)
        
        rec.cache_clear()
        return ans
