# Last updated: 27/10/2025, 2:51:35 pm
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])

        ans = 0
        prev = -1
        for i in range(m):
            cam = bank[i].count('1')
            if cam == 0: continue
            if prev != -1:
                ans += cam * prev
            prev = cam
        
        return ans