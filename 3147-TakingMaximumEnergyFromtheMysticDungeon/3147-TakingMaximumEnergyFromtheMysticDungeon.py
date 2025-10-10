# Last updated: 10/10/2025, 1:30:46 pm
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        
        best = -inf
        for i in range(n-1, n-k-1, -1):
            s = 0
            for j in range(i, -1, -k):
                s += energy[j]
                best = max(s, best)
        
        return best