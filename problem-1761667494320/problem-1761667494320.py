# Last updated: 28/10/2025, 9:34:54 pm
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        left = [-2] * n
        left.append(-1)
        index = 0
        for i in range(m):
            if s[i] == t[index]:
                left[index] = i
                index += 1
                if index == n:
                    return 0

        right = [-2] * n
        right.append(m)
        index = n-1
        for i in range(m-1, -1, -1):
            if s[i] == t[index]:
                right[index] = i
                index -= 1
                if index == -1:
                    return 0

        
        def isGood(mid):
            if mid == n: return True
            for i in range(mid, n + 1):
                l = i - mid - 1
                r = i
                
                # print((l, r), (t[:l + 1], t[r:]), mid)
                if left[l] != -2 and right[r] != -2 and left[l] < right[r]:
                    return True
            return False
        
        l = 1
        r = n

        # print(left)
        # print(right)
        
        while l < r:
            mid = (l + r) // 2
            # print(l, mid, r)
            if isGood(mid):
                r = mid
            else:
                l = mid + 1

        return l
            