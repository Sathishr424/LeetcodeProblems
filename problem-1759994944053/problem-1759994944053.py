# Last updated: 9/10/2025, 12:59:04 pm
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        m = len(word1)
        n = len(word2)

        word1 = [ord(a) - ord('a') for a in word1]
        word2 = [ord(a) - ord('a') for a in word2]

        f1 = [0] * 26
        f2 = [0] * 26

        for a in word1:
            f1[a] += 1
        for a in word2:
            f2[a] += 1

        def check(a1, a2):
            if not f1[a1] or not f2[a2]: return False

            f1[a1] -= 1
            f1[a2] += 1
            f2[a2] -= 1
            f2[a1] += 1
            
            cnt = 0
            for a in range(26):
                if f1[a]:
                    cnt += 1

            for a in range(26):
                if f2[a]:
                    cnt -= 1
                
            f1[a1] += 1
            f1[a2] -= 1
            f2[a2] += 1
            f2[a1] -= 1

            return cnt == 0

        for i in range(26):
            for j in range(26):
                if check(i, j): return True

        return False