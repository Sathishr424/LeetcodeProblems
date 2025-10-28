# Last updated: 28/10/2025, 9:43:19 pm
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        left = [m] * n
        index = 0
        for i in range(m):
            if s[i] == t[index]:
                left[index] = i
                index += 1
                if index == n:
                    return 0

        right = [-1] * n
        index = n-1
        for i in range(m-1, -1, -1):
            if s[i] == t[index]:
                right[index] = i
                index -= 1
                if index == -1:
                    return 0
        
        def isGood(mid):
            if right[mid] != -1: return True
            if left[n-mid-1] != m: return True
            for i in range(mid + 1, n):
                l = i - mid - 1
                r = i
                
                if left[l] < right[r]:
                    return True
            
            return False
        
        l = 1
        r = n
        
        while l < r:
            mid = (l + r) // 2

            if isGood(mid):
                r = mid
            else:
                l = mid + 1

        return l
            