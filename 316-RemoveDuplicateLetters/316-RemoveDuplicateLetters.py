# Last updated: 9/4/2025, 9:52:13 pm
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)

        uniq = defaultdict(int)
        for char in s: uniq[char] += 1

        stack = []
        there = {}
        
        for i in range(n):
            char = s[i]
            if char in there: 
                uniq[char] -= 1
                continue
            
            while stack and stack[-1] > char:
                if uniq[stack[-1]] <= 0: break
                del there[stack.pop()]
            
            there[char] = 1
            stack.append(char)
            uniq[char] -= 1
        
        return ''.join(stack)
        