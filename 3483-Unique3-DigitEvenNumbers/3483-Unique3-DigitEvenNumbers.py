# Last updated: 12/5/2025, 1:30:19 pm
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for num in digits:
            freq[num] += 1
        
        ret = 0

        for i in range(1, 10):
            if freq[i] == 0: continue
            freq[i] -= 1
            for j in range(10):
                if freq[j] == 0: continue
                freq[j] -= 1
                for k in range(0, 10, 2):
                    if freq[k]: ret += 1
                freq[j] += 1
            freq[i] += 1

        return ret
        