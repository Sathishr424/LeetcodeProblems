# Last updated: 15/6/2025, 8:38:56 am
N = 82
dp = [[{} for _ in range(10)] for _ in range(N)]

def rec(s, p, rem):
    if p in dp[s][rem]: return dp[s][rem][p]
    if rem == 0:
        if p % s == 0: return 1
        return 0

    ans = 1 if p % s == 0 else 0
    for i in range(10):
        ans += rec(s + i, p * i, rem - 1)
    dp[s][rem][p] = ans
    return ans

for i in range(1, 10):
    rec(i, i, 8)

def getCount(r):
    if r == 0: return 0
    arr = [int(a) for a in list(str(r))]
    n = len(arr)
    ret = 0
    
    for i in range(1, arr[0]):
        curr = rec(i, i, n-1)
        ret += curr
    
    if n > 1:
        for i in range(arr[0], 10):
            curr = rec(i, i, n-2)
            ret += curr
    
    @cache
    def dfs(s, p, rem):
        if rem == 0:
            return 1 if p % s == 0 else 0
        
        ans = 0
        for i in range(10):
            ans += dfs(s + i, p * i, rem - 1)
        return ans
    
    s = arr[0]
    p = arr[0]
    balance = 0
    for i in range(1, n):
        num = arr[i]
        for j in range(num):
            curr = dfs(s + j, p * j, n-i-1)
            balance += curr
    
        s += num
        p *= num
    
    balance += p % s == 0
    return ret + balance

class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        return getCount(r) - getCount(l-1)