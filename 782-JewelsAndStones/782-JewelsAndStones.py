# Last updated: 12/6/2025, 5:46:51 am
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ret = 0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i] == jewels[j]: ret+=1
        return ret