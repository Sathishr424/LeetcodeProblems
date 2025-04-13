# Last updated: 13/4/2025, 9:45:03 am
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        u = defaultdict(int)
        for char in s:
            u[char] += 1

        s = sorted(u.keys())
        
        ret = ''
        smallest = ''
        for a in s:
            if u[a] % 2 == 1:
                smallest = a
            ret += a * (u[a] // 2)
            
        ret = ret + smallest + ret[::-1]
        return ret
                