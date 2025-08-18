# Last updated: 18/8/2025, 7:33:28 pm
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        
        total = sum(nums)
        if total == 0 and n > 1: return True
        nums.sort()
        av = total / n
        
        @cache
        def rec(index, rem, rem_cnt):
            if rem == 0: 
                if rem_cnt == 0: return True
                return False
        
            if rem_cnt == 0 or index == n: return False
            
            if rem < nums[index]: return False
            if rec(index + 1, rem, rem_cnt) or rec(index + 1, rem - nums[index], rem_cnt-1): return True
            
            return False

        for i in range(1, n):
            need = round(av * i, 5)
            if need - int(need) == 0:
                rem = total - need
                if rem / (n - i) == av and rec(0, int(need), i): 
                    return True

        rec.cache_clear()
        return False
        
        