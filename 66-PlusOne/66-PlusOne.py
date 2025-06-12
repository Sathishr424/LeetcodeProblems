# Last updated: 12/6/2025, 5:54:05 am
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i >= 0:
            if digits[i]+1 < 10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
        digits[0] = 0
        return [1] + digits
                
