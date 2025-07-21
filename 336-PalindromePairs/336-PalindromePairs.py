# Last updated: 21/7/2025, 11:12:02 pm
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        forwards = {}
        ret = []
        visited = {}

        def checkPalForward(i, word):
            for j in range(len(word), -1, -1):
                left = word[j:][::-1]
                curr = left + word
                if curr == curr[::-1]:
                    if left in forwards and forwards[left] != i:
                        visited[(forwards[left], i)] = 1
            
        def checkPalReverse(i, word):
            for j in range(len(word) + 1):
                right = word[:j][::-1]
                curr = word + right
                if curr == curr[::-1]:
                    if right in forwards and forwards[right] != i:
                        visited[(i, forwards[right])] = 1
        
        for i, word in enumerate(words):
            forwards[word] = i
        
        for i, word in enumerate(words):
            checkPalForward(i, word)
            checkPalReverse(i, word)
        
        for i, j in visited:
            ret.append([i, j])

        return ret