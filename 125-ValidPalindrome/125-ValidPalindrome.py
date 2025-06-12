# Last updated: 12/6/2025, 5:52:42 am
valid = set(list('abcdefghijklmnopqrstuvwxyz1234567890'))
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            left = s[l].lower()
            right = s[r].lower()
            if right not in valid:
                r -= 1
            elif left not in valid:
                l += 1
            elif left == right:
                    l += 1
                    r -= 1
            else: return False
        return True