# Last updated: 12/6/2025, 5:36:11 am
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        ret = [words[0]]
        prev = groups[0]
        
        for i in range(1, n):
            if groups[i] != prev:
                ret.append(words[i])
                prev = groups[i]
        
        return ret
