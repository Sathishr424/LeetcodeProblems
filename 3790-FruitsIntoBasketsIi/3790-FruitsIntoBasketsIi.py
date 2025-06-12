# Last updated: 12/6/2025, 5:34:14 am
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for q in baskets:
            for i in range(len(fruits)):
                if fruits[i] <= q:
                    fruits = fruits[:i] + fruits[i+1:]
                    break
        
        return len(fruits)