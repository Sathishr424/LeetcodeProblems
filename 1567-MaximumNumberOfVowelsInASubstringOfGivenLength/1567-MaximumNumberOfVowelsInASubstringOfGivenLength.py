# Last updated: 12/6/2025, 5:41:32 am
vov = ['a','e','i','o','u']

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxi = 0
        ones = False
        maxCnt = 0
        for i in range(len(s)-(k-1)):
            if ones:
                maxCnt = (maxCnt - (s[i-1] in vov)) + (s[i+(k-1)] in vov)
            else:
                for i in s[i:i+k]:
                    if i in vov: maxCnt += 1
            maxi = max(maxCnt,maxi)
            if not ones: ones = True
            if maxi == k: return maxi
        return maxi