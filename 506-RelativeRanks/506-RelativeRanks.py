# Last updated: 12/6/2025, 5:48:46 am
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        holder = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = len(score)
        
        ret = []
        tmp = []
        for i in range(n):
            tmp.append((score[i], i))
            ret.append("")
        
        tmp.sort(reverse=True, key=lambda x: x[0])
        
        for i in range(min(3, n)):
            ret[tmp[i][1]] = holder[i]
        
        for i in range(3, n):
            ret[tmp[i][1]] = str(i+1)

        return ret