# Last updated: 5/8/2025, 10:35:45 am
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)

        used = [0] * n

        for f in fruits:
            for i in range(n):
                if used[i] == 0 and baskets[i] >= f:
                    used[i] = 1
                    break
        
        return n - sum(used)