# Last updated: 31/5/2025, 9:52:10 pm
@cache
def getComb(x, y):
    if x == 0 and y == 0: return 1
    elif x == 0: return 0
    return x * getComb(y, x-1)

class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        odds = []
        evens = []

        for i in range(1, n+1):
            if i % 2:
                odds.append(i)
            else:
                evens.append(i)
        
        def dfs(evens, odds, k):
            f = getComb(len(odds), len(evens)-1)
            p = 0
            for i in range(len(evens)):
                if p+f >= k:
                    return [evens[i]] + dfs(odds, evens[:i] + evens[i+1:], k-p)
                p += f
            
            return []
        
        p = 0
        ret = []
        for i in range(1, n+1):
            half = (i-1)//2
            if i % 2 == 0:
                f = getComb(len(odds), len(evens)-1)
                if f + p >= k:
                    ret = [evens[half]] + dfs(odds, evens[:half] + evens[half+1:], k-p)
                    break
            else:
                f = getComb(len(evens), len(odds)-1)
                if f + p >= k:
                    odds, evens = evens, odds
                    ret = [evens[half]] + dfs(odds, evens[:half] + evens[half+1:], k-p)
                    break
            p += f

        return ret