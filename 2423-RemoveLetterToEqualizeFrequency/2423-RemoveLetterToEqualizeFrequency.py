# Last updated: 24/9/2025, 9:35:44 pm
class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)

        for i in range(n):
            freq = defaultdict(int)
            for j in range(n):
                if i == j: continue
                freq[word[j]] += 1

            cnts = sorted(freq.values())
            if cnts[0] == cnts[-1]: return True

        return False