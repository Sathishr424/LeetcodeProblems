# Last updated: 12/6/2025, 5:39:42 am
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = []
        for s in sentence:
            if s not in cnt: cnt.append(s)
        if len(cnt) == 26: return True
        return False