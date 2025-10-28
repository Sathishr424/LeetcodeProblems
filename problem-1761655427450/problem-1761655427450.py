# Last updated: 28/10/2025, 6:13:47 pm
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)

        prefix = [0]
        vowel = 'aeiou'
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])

        return ans