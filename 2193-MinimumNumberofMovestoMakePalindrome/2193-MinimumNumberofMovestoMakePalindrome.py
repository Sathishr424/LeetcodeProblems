# Last updated: 26/8/2025, 10:00:42 pm
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        s = list(s)
        for char in s:
            counts[char] += 1

        l = 0
        r = len(s) - 1
        op = 0
        while l < r:
            if s[l] != s[r]:
                if counts[s[l]] == 1:
                    s[l], s[l+1] = s[l+1], s[l]
                    op += 1
                    continue
                else:
                    for j in range(r, l, -1):
                        if s[j] == s[l]:
                            for k in range(j, r):
                                s[k], s[k + 1] = s[k+1], s[k]
                                op += 1
                            break
            counts[s[l]] -= 2
            l += 1
            r -= 1

        return op