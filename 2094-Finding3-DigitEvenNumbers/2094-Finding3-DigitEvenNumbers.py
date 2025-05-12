# Last updated: 12/5/2025, 1:22:36 pm
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for num in digits:
            freq[num] += 1
        
        ret = []

        for i in range(1, 10):
            if freq[i] == 0: continue
            freq[i] -= 1
            for j in range(10):
                if freq[j] == 0: continue
                freq[j] -= 1
                for k in range(0, 10, 2):
                    if freq[k]:
                        ret.append((i * 100) + (j * 10) + k)
                freq[j] += 1
            freq[i] += 1

        return ret
