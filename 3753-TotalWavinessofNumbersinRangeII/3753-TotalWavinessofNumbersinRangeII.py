# Last updated: 22/11/2025, 11:41:23 pm
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(num):
            nums = [int(d) for d in str(num)]
            n = len(nums)

            @cache
            def rec(index, prev_prev, prev, strict, w, is_zero):
                if index == n:
                    return w
                
                l = 0
                r = nums[index] + 1 if strict else 10
                ans = 0

                for i in range(l, r):
                    if is_zero and i == 0:
                        ans += rec(index + 1, -1, -1, False, 0, True)
                    elif prev_prev != -1 and ((prev > prev_prev and prev > i) or (prev < prev_prev and prev < i)):
                        ans += rec(index + 1, prev, i, strict and i == nums[index], w + 1, False)
                    else:
                        ans += rec(index + 1, prev, i, strict and i == nums[index], w, False)
                return ans
            
            ans = rec(0, -1, -1, True, 0, True)
            rec.cache_clear()
            return ans
        
        return calc(num2) - calc(num1 - 1)