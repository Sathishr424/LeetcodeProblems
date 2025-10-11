# Last updated: 11/10/2025, 8:04:04 pm
class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)
        s = [ord(a) - ord('a') + 1 for a in s]
        # print(s)
        left = 0
        for i in range(n):
            left += s[i]
            right = 0
            for j in range(i+1, n):
                right += s[j]
            # print(i, left, right)
            if left == right:
                return True
        return False