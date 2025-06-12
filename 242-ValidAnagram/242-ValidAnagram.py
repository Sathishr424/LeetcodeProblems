# Last updated: 12/6/2025, 5:51:07 am
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alp = [0] * 26

        for char in s:
            alp[ord(char) - 97] += 1
        for char in t:
            if alp[ord(char) - 97] == 0: return False
            alp[ord(char) - 97] -= 1
        for i in range(26):
            if alp[i] > 0: return False
        return True