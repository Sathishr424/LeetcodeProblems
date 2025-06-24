# Last updated: 24/6/2025, 5:36:25 pm
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)

        new_a = a + (a * ceil(m / n))
        for i in range(n):
            if a[i] == b[0]:
                if new_a[i:i+m] == b:
                    l = m - (n - i)
                    return ceil(l / n) + 1
        
        return -1
