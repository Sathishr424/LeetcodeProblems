# Last updated: 4/6/2025, 2:59:29 am
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        n = len(word)
        indexes = []

        maxi = 0
        for i, char in enumerate(word):
            if char > word[maxi]:
                maxi = i
        
        split = n - (numFriends - 1)
        ret = word[maxi:maxi+split]
        for i, char in enumerate(word):
            if char == word[maxi]:
                ret = max(ret, word[i:i+split])
        
        return ret

            