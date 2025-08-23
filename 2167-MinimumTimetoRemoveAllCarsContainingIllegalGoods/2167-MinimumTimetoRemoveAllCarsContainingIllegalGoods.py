# Last updated: 24/8/2025, 1:54:47 am
class Solution:
    def minimumTime(self, s: str) -> int:
        # s = [str(random.randrange(2)) for _ in range(10**5 * 2)]
        n = len(s)

        left = []
        l = 0
        add = 0
        for i in range(n):
            add += 1
            if s[i] == '1':
                l += add
                add = 0
            left.append(l)

        right = [0] * n
        r = 0
        add = 0
        for i in range(n-1, -1, -1):
            add += 1
            if s[i] == '1':
                r += add
                add = 0
            right[i] = r

        @cache
        def rec(index):
            if index == n: return 0

            if s[index] == '1':
                return min(right[index], 2 + rec(index + 1))
            else:
                return rec(index + 1)
        
        ans = inf
        for i in range(n):
            curr = rec(i)
            ans = min(ans, (left[i-1] if i > 0 else 0) + rec(i))
            # print(i, curr, left[i-1] + rec(i))
        
        return ans