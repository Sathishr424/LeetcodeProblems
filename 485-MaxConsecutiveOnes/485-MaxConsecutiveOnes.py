# Last updated: 12/6/2025, 5:49:03 am
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        maxi = 0
        there = False
        for i in nums:
            if i == 1:
                if not there:
                    there = True
                    ret = 1
                else:
                    ret += 1
            else:
                if ret > maxi: 
                    maxi = ret
                there = False
        if there and ret > maxi: maxi = ret
        return maxi