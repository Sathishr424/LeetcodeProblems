# Last updated: 12/6/2025, 5:40:57 am
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        curr = neededTime[0]
        currTotal = neededTime[0]

        ret = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                curr = max(curr, neededTime[i])
                currTotal += neededTime[i]
            else:
                ret += currTotal - curr
                curr = neededTime[i]
                currTotal = neededTime[i]

        return ret + currTotal - curr

