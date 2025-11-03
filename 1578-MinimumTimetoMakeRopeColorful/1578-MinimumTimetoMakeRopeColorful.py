# Last updated: 3/11/2025, 10:31:06 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        
        maxTime = neededTime[0]
        time = 0
        for i in range(1, n):
            if colors[i] != colors[i - 1]:
                time += maxTime
                maxTime = neededTime[i]
            else:
                maxTime = cmax(maxTime, neededTime[i])
        
        return sum(neededTime) - time - maxTime
