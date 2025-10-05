# Last updated: 5/10/2025, 7:24:08 am
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        n = len(s)

        # left = abc
        # right = abc
        # left = a, b, c right = bc, ab, ac
        # let = bc, ab, ac, right = c, a, b
        best = inf
        a = 0
        b = 0
        c = 0
        p_a = [inf] * (n + 1)
        p_b = [inf] * (n + 1)
        p_c = [inf] * (n + 1)
        p_a[0] = 0
        p_b[0] = 0
        p_c[0] = 0
        for i in range(n):
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                b += 1
            elif s[i] == 'c':
                c += 1

            p_a[a] = min(p_a[a], i + 1)
            p_b[b] = min(p_b[b], i + 1)
            p_c[c] = min(p_c[c], i + 1)
            if a >= k and b >= k and c >= k:
                best = min(best, i + 1)

        a = 0
        b = 0
        c = 0
        for i in range(n-1, -1, -1):
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                b += 1
            elif s[i] == 'c':
                c += 1

            a_need = max(0, k - a)
            b_need = max(0, k - b)
            c_need = max(0, k - c)

            index = max(p_a[a_need], p_b[b_need], p_c[c_need])
            if index < i:
                best = min(best, index + (n - i))

        return -1 if best == inf else best