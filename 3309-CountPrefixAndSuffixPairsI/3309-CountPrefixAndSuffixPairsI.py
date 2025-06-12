# Last updated: 12/6/2025, 5:35:51 am
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ret = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if len(words[i]) > len(words[j]): continue
                t = len(words[i])
                r = len(words[j])-1

                ret += 1

                for k in range(t):
                    if words[i][k] != words[j][k] or words[i][t-k-1] != words[j][r]:
                        ret -= 1
                        break
                    r -= 1
        
        return ret