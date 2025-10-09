# Last updated: 9/10/2025, 9:32:23 am
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        ret = ''
        for c, cnt in stack:
            ret += c * cnt
        return ret