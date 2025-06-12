# Last updated: 12/6/2025, 5:39:13 am
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hash = {}

        for num in nums:
            hash[num] = 1
        n = len(nums[0])
        ret = ''
        def rec(st):
            nonlocal ret
            if len(st) == n:
                if st not in hash:
                    ret = st
                    return True
                return False
            
            if rec(st + '0'): return True
            if rec(st + '1'): return True

            return False
        
        rec('')
        return ret