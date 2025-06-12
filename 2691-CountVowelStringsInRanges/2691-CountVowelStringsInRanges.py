# Last updated: 12/6/2025, 5:37:15 am
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixSum = []
        vowels = ['a','e','i','o','u']

        curr = 0

        for i in range(len(words)):
            curr += words[i][0] in vowels and words[i][-1] in vowels
            prefixSum.append(curr)

        ret = []

        for x, y in queries:
            ret.append(prefixSum[y] - (prefixSum[x-1] if x-1 >= 0 else 0))
        
        return ret
