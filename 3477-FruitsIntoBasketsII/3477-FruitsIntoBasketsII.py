# Last updated: 6/6/2025, 11:34:45 pm
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        
        for q in baskets:
            for i in range(len(fruits)):
                if fruits[i] <= q:
                    fruits = fruits[:i] + fruits[i+1:]
                    break
        
        return len(fruits)