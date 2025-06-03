# Last updated: 4/6/2025, 2:23:44 am
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        n = len(word)
        indexes = []

        maxi = 0
        for i, char in enumerate(word):
            if char > word[maxi]:
                maxi = i
        
        for i, char in enumerate(word):
            if char == word[maxi]:
                indexes.append(i)
        
        split = n - (numFriends-1)

        def checkMax(i, j):
            k = min(n, i+split)
            l = min(n, j+split)
            while i < k and j < l:
                if word[i] > word[j]: return True
                elif word[j] > word[i]: return False
                i += 1
                j += 1
            
            return False

        start = indexes[0]
        
        for index in indexes[1:]:
            if checkMax(index, start):
                start = index

        return word[start:start+split]

            