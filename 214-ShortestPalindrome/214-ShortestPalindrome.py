# Last updated: 24/4/2025, 7:12:27 pm
mod= 10**9 + 7
base = 28

def modInverse(num):
    return pow(num, mod-2, mod)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        def addNum(num, val):
            return ((num * base % mod) + val) % mod
        
        def addLeft(num, val, distance):
            return (num + (val * pow(base, distance, mod) % mod)) % mod
        
        def deleteRight(num, val):
            num -= val
            return num * modInverse(base) % mod
        
        def deleteLeft(num, val, distance):
            return (num - ( val * pow(base, distance, mod) % mod) ) % mod
        
        left = 0
        right = 0

        for i in range(n // 2):
            left = addNum(left, ord(s[i]) - 96)
            right = addNum(right, ord(s[n-i-1]) - 96)

        alt = True
        if n % 2:
            alt = False

        if left == right: return s
        
        l_pos = [0, n//2 - 1]
        r_pos = [(n+1) // 2, n-1]

        while l_pos[1] >= 0:
            # print(l_pos, r_pos, s[:l_pos[1]+1], s[r_pos[0]:r_pos[1]+1], (left, right), alt)
            right = deleteLeft(right, ord(s[r_pos[1]]) - 96, r_pos[1] - r_pos[0])
            r_pos[1] -= 1
            if not alt:
                r_pos[0] -= 1
                right = addNum(right, ord(s[r_pos[0]]) - 96)
                alt = True
            else:
                left = deleteRight(left, ord(s[l_pos[1]]) - 96)
                l_pos[1] -= 1
                alt = False
            if left == right: return s[r_pos[1]+1:][::-1] + s

        return ''