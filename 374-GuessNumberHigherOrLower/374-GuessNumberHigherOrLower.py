# Last updated: 12/6/2025, 5:50:03 am
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        
        while l <= r:
            mid = (l+r) // 2
            ans = guess(mid)

            if ans == -1:
                r = mid-1
            elif ans == 1:
                l = mid+1
            else:
                return mid