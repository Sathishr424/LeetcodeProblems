# Last updated: 8/10/2025, 3:07:59 pm
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        m = len(spells)
        n = len(potions)

        potions.sort()

        ans = [0] * m
        for i in range(m):
            spell = spells[i]
            l = 0
            r = n

            while l < r:
                mid = (l + r) // 2

                if potions[mid] * spell >= success:
                    r = mid
                else:
                    l = mid + 1
            
            ans[i] = n - l
        
        return ans