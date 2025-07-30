# Last updated: 30/7/2025, 5:00:34 pm
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        n = len(customers)

        max_profit = -1
        best_rotation = -1
        
        waitList = 0
        total = 0
        g = [0] * 4
        index = 0
        rotation = 0
        for i, c in enumerate(customers):
            waitList += c

            possible = min(4, waitList)
            g[index] = possible
            waitList -= possible

            total += boardingCost * possible
            
            index = (index + 1) % 4
            total -= runningCost
            
            rotation += 1

            if total > max_profit:
                max_profit = total
                best_rotation = rotation

        while waitList:
            possible = min(4, waitList)
            g[index] = possible
            waitList -= possible

            total += boardingCost * possible
            
            index = (index + 1) % 4
            total -= runningCost
            rotation += 1

            if total > max_profit:
                max_profit = total
                best_rotation = rotation
        
        return best_rotation if max_profit > 0 else -1