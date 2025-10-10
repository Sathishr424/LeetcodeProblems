# Last updated: 10/10/2025, 1:38:46 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        
        best = -inf
        for i in range(n-1, n-k-1, -1):
            s = 0
            for j in range(i, -1, -k):
                s += energy[j]
                best = cmax(s, best)
        
        return best