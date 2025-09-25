# Last updated: 26/9/2025, 2:16:59 am
class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words)
        there = defaultdict(list)

        for word in words:
            key = ''
            for i in range(1, len(word)):
                key += str((ord(word[i]) - ord('a')) - (ord(word[i - 1]) - ord('a'))) + ','
            there[key].append(word)

        for key in there:
            if len(there[key]) == 1:
                return there[key][0]

        return words[0]