# Last updated: 10/10/2025, 1:27:30 pm
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # energy = [random.randrange(-1000, 1001) for _ in range(10**5)]
        n = len(energy)
        
        @cache
        def rec(index):
            if index >= n: return 0
            
            return rec(index + k) + energy[index]
        
        best = -inf
        for i in range(n):
            best = max(best, rec(i))
        
        return best