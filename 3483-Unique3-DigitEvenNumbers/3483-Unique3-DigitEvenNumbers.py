# Last updated: 12/5/2025, 1:37:33 pm
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for num in digits:
            freq[num] += 1
        
        ret = 0

        def check(num):
            if num == 0: return True
            rem = num % 10
            if freq[rem] == 0: return False
            freq[rem] -= 1
            ans = check(num // 10)
            freq[rem] += 1
            return ans

        for num in range(100, 999, 2):
            ret += check(num)
        
        return ret
        