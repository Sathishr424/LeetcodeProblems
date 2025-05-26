# Last updated: 26/5/2025, 11:16:31 pm
# abcdefghihklmnoopqrstwxyz
@cache
def isPair(x, y):
    x = ord(x) - 97
    y = ord(y) - 97

    if (x + 1) % 26 == y or (x - 1) % 26 == y:
        return True
    return False

class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)     
        @cache
        def dfs(i, j):
            if i == j: return False
            elif i > j: return True
            if isPair(s[i], s[j]) and dfs(i+1, j-1):
                return True
            if (j-i+1) % 2: return False
            for k in range(i+1, j, 2):
                if dfs(i, k) and dfs(k+1, j): return True
            return False

        @cache
        def rec(index):
            if index == n: return ''

            ans = s[index] + rec(index+1)

            for i in range(index+1, n, 2):
                if dfs(index, i):
                    ans = min(ans, rec(i+1))
            
            return ans
        
        return rec(0)
