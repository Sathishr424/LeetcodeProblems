# Last updated: 12/6/2025, 5:39:29 am
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hash = defaultdict(int)
        n = len(words)

        for word in words:
            for char in word:
                hash[char] += 1

        for char in hash:
            if hash[char] % n != 0: return False
        
        return True