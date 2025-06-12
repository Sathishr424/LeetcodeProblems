# Last updated: 12/6/2025, 5:39:30 am
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        k = len(part)
        half = ceil(k/2)
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= k:
                j = 0
                while j < half and stack[-k+j] == part[j] and stack[-j-1] == part[k-j-1]:
                    j += 1
                
                if j == half: 
                    for _ in range(k): stack.pop()
        
        return ''.join(stack)

                    
