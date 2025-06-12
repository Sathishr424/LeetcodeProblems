# Last updated: 12/6/2025, 5:40:45 am
class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        ret = 0
        for i in s:
            if i == '(': cnt += 1
            elif i == ')': cnt -= 1
            if cnt > ret: ret = cnt
        return ret