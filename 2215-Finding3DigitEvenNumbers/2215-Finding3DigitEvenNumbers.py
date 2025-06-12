# Last updated: 12/6/2025, 5:38:54 am
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for num in digits:
            freq[num] += 1
        
        ret = []

        for i in range(1, 10):
            if freq[i] == 0: continue
            for j in range(10):
                if freq[j] == 0: continue
                for k in range(0, 10, 2):
                    if freq[k] == 0: continue
                    
                    if i == j and j == k:
                        if freq[i] < 3: continue
                    elif i == j or i == k:
                        if freq[i] < 2: continue
                    elif j == k:
                        if freq[j] < 2: continue
                    
                    ret.append((i * 100) + (j * 10) + k)
        return ret