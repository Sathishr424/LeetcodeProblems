# Last updated: 4/6/2025, 2:20:00 am
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

        def checkMax(x, y):
            for i in range(min(len(x), len(y))):
                if x[i] > y[i]: return True
                elif y[i] > x[i]: return False
            
            return False

        index = indexes[0]
        ret = word[index:index+split]
        for index in indexes[1:]:
            curr = word[index:index+split]
            if checkMax(curr, ret):
                ret = curr

        return ret

            