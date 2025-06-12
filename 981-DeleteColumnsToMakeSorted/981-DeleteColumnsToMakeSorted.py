# Last updated: 12/6/2025, 5:45:00 am
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ret = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if ord(strs[j][i]) < ord(strs[j-1][i]):
                    ret += 1
                    break
        
        return ret
