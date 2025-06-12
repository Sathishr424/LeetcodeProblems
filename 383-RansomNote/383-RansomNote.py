# Last updated: 12/6/2025, 5:50:00 am
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alp = [0] * 26
        for char in magazine:
            alp[ord(char) - 97] += 1
        for char in ransomNote:
            if alp[ord(char) - 97] == 0: return False
            alp[ord(char) - 97] -= 1
        return True