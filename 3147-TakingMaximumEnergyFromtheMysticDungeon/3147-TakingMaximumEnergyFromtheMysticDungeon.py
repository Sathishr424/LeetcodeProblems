# Last updated: 10/10/2025, 1:28:10 pm
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        
        cache = [-inf] * n
        def rec(index):
            if index >= n: return 0
            if cache[index] != -inf: return cache[index]
            
            cache[index] = rec(index + k) + energy[index]
            return cache[index]
        
        best = -inf
        for i in range(n):
            best = max(best, rec(i))
        
        return best