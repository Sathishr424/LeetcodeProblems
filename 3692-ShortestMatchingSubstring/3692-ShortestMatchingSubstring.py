# Last updated: 12/6/2025, 5:35:04 am
def getLps(x):
    n = len(x)

    lps = [0] * n
    i = 1
    j = 0

    while i < n:
        if x[i] == x[j]:
            j += 1
            lps[i] = j
        elif j != 0:
            j = lps[j-1]
            continue
        i += 1
    return lps

def getMatch(x, y):
    lps = getLps(y)

    j = 0
    ret = []
    i = 0
    while i < len(x):
        if x[i] == y[j]:
            j += 1
            if j == len(y):
                ret.append((i-j+1, i))
                j = lps[j-1]
        elif j != 0: 
            j = lps[j-1]
            continue
        i += 1
    return ret

def bn(arr, val):
    l = 0
    r = len(arr)

    while l < r:
        mid = (l+r) // 2

        if arr[mid][0] > val:
            r = mid
        else:
            l = mid+1
    
    return l
    
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        if p == '**': return 0
        m = len(s)
        n = len(p)

        left = []
        mid = []
        right = []

        first_star = p.find('*')
        second_star = n
        for i in range(first_star+1, n):
            if p[i] == '*':
                second_star = i
                break

        matches = 3
        if first_star != 0:
            to_find = p[:first_star]
            left = getMatch(s, to_find)
            matches -= not left
        
        if second_star-first_star > 1:
            to_find = p[first_star+1:second_star]
            mid = getMatch(s, to_find)
            matches -= not mid
        
        if second_star != n-1:
            to_find = p[second_star+1:]
            right = getMatch(s, to_find)
            matches -= not right
        
        if matches != 3: return -1

        arr = []

        if left: arr.append(left)
        if mid: arr.append(mid)
        if right: arr.append(right)
            
        ret = float('inf')

        for x, y in arr[0]:
            left = x
            right = y
            match = True
            for i in range(1, len(arr)):
                index = bn(arr[i], right)
                if index == len(arr[i]):
                    match = False
                    break
                right = arr[i][index][1]
            
            if match:
                ret = min(ret, right-left+1)
        
        return ret if ret != float('inf') else -1 