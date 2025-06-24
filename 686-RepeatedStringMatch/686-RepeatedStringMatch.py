# Last updated: 24/6/2025, 5:34:41 pm
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)

        new_a = a + (a * ceil(m / n))
        for i in range(n):
            if a[i] == b[0]:
                l = m - (n - i)
                if new_a[i:i+m] == b:
                    return ceil(l / n) + 1
        
        return -1
