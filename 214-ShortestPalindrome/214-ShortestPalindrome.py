# Last updated: 24/4/2025, 7:22:38 pm
mod= 10**9 + 7
base = 28
inverseBase = pow(base, mod-2, mod)

def addNum(num, val):
    return ( (num * base % mod) + val ) % mod

def deleteRight(num, val):
    num -= val
    return num * inverseBase % mod

def deleteLeft(num, val, distance):
    return (num - ( val * pow(base, distance, mod) % mod) ) % mod

def getAlpIndex(val):
    return ord(val) - 96

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        
        left = 0
        right = 0

        for i in range(n // 2):
            left = addNum(left, getAlpIndex(s[i]))
            right = addNum(right, getAlpIndex(s[n-i-1]))

        if left == right: return s

        isOddTurn = n % 2 != 1
        
        l_pos = [0, n//2 - 1]
        r_pos = [(n+1) // 2, n-1]

        while l_pos[1] >= 0:
            right = deleteLeft(right, getAlpIndex(s[r_pos[1]]), r_pos[1] - r_pos[0])
            r_pos[1] -= 1
            if not isOddTurn:
                r_pos[0] -= 1
                right = addNum(right, getAlpIndex(s[r_pos[0]]))
                isOddTurn = True
            else:
                left = deleteRight(left, getAlpIndex(s[l_pos[1]]))
                l_pos[1] -= 1
                isOddTurn = False
            if left == right: return s[r_pos[1]+1:][::-1] + s

        return ''