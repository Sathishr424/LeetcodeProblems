# Last updated: 12/6/2025, 5:37:21 am
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1
        right = min(ranks) * cars * cars

        while left < right:
            minutes = (left+right) // 2

            ans = 0
            for rank in ranks:
                ans += int(sqrt(minutes / rank))
            
            if ans >= cars:
                right = minutes
            else:
                left = minutes+1
        
        return left
                
