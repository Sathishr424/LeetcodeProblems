# Last updated: 21/7/2025, 11:00:07 pm
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        forwards = defaultdict(list)
        ret = []
        visited = {}

        def checkPalForward(i, word):
            for j in range(len(word), -1, -1):
                left = word[j:][::-1]
                curr = left + word
                if curr == curr[::-1]:
                    for index in forwards[left]:
                        if index == i or (index, i) in visited: continue
                        visited[(index, i)] = 1
            
        def checkPalReverse(i, word):
            for j in range(len(word) + 1):
                right = word[:j][::-1]
                curr = word + right
                if curr == curr[::-1]:
                    for index in forwards[right]:
                        if index == i or (i, index) in visited: continue
                        visited[(i, index)] = 1
        
        for i, word in enumerate(words):
            forwards[word].append(i)
        
        for i, word in enumerate(words):
            checkPalForward(i, word)
            checkPalReverse(i, word)
        
        for i, j in visited:
            ret.append([i, j])

        return ret