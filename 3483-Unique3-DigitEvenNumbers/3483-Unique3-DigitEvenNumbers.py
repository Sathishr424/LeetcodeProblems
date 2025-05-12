# Last updated: 12/5/2025, 2:09:56 pm
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for num in digits:
            freq[num] += 1
        
        ret = 0

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
                    
                    ret += 1
        return ret
        