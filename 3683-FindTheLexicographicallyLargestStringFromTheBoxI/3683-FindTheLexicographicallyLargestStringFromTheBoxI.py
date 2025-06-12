# Last updated: 12/6/2025, 5:35:07 am
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        split = len(word) - (numFriends - 1)

        maxi = 0
        for i, char in enumerate(word):
            if char > word[maxi]:
                maxi = i
        
        ret = word[maxi:maxi+split]
        for i, char in enumerate(word):
            if char == word[maxi]:
                ret = max(ret, word[i:i+split])
        
        return ret

            