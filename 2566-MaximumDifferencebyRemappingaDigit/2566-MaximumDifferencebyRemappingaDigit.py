# Last updated: 14/6/2025, 1:55:54 pm
def gcd(x, y):
    rem = x % y
    if rem == 0: return y

    return gcd(y, rem)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: return ''
        n = len(str1)
        m = len(str2)
        if m > n:
            n, m = m, n
        return str1[0:gcd(n, m)]