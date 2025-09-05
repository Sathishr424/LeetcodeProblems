# Last updated: 5/9/2025, 1:27:54 pm
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        lookup = []
        next_index = []
        for i in range(n):
            n_index = len(lookup) + len(piles[i])
            for pile in piles[i]:
                lookup.append(pile)
                next_index.append(n_index)
        
        n = len(lookup)
        @cache
        def rec(index, rem):
            if rem == 0: return 0
            if index >= n: return -inf

            ans = rec(next_index[index], rem)
            ans = max(ans, rec(index + 1, rem - 1) + lookup[index])

            return ans

        ans = rec(0, k)
        rec.cache_clear()
        return ans

                