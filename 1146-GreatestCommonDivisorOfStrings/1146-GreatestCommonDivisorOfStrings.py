# Last updated: 12/6/2025, 5:43:53 am
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str2)
        m = len(str1)
        hash = defaultdict(int)

        for i in range(1, m+1):
            if m % i != 0: continue
            curr = str1[i-i:i]
            match = True

            for j in range(i, m-i+1, i):
                if curr != str1[j:j+i]: 
                    match = False
                    break
            
            if match:
                hash[curr] = 1

        maxi = 0
        ans = ""

        for i in range(1, n+1):
            if n % i != 0: continue
            curr = str2[i-i:i]
            match = True
            
            for j in range(i, n-i+1, i):
                if curr != str2[j:j+i]: 
                    match = False
                    break
            
            if match and curr in hash and len(curr) > maxi:
                ans = curr

        return ans