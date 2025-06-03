# Last updated: 4/6/2025, 2:59:54 am
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

            