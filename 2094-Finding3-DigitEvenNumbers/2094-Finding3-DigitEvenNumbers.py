# Last updated: 12/5/2025, 1:36:44 pm
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for num in digits:
            freq[num] += 1
        
        ret = []

        def check(num):
            if num == 0: return True
            rem = num % 10
            if freq[rem] == 0: return False
            freq[rem] -= 1
            ans = check(num // 10)
            freq[rem] += 1
            return ans

        for num in range(100, 999, 2):
            if check(num): ret.append(num)
        
        return ret
            

