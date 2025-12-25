# Last updated: 12/25/2025, 7:11:59 PM
class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        
        right = [0] * n
        for i in range(n-2, -1, -1):
            cnt = -1
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    break
                cnt = j
            right[i] = max(right[i + 1], cnt + 1)

        left = [0] * n
        for i in range(1, n):
            cnt = -1
            for j in range(min(len(words[i]), len(words[i-1]))):
                if words[i][j] != words[i-1][j]:
                    break
                cnt = j
            left[i] = max(left[i - 1], cnt + 1)

        ret = []
        for i in range(n):
            curr = 0
            if i + 1 < n:
                curr = max(curr, right[i + 1])
            if i - 1 >= 0:
                curr = max(curr, left[i - 1])
            cnt = -1
            if i + 1 < n and i - 1 >= 0:
                for j in range(min(len(words[i-1]), len(words[i+1]))):
                    if words[i - 1][j] != words[i+1][j]:
                        break
                    cnt = j
            curr = max(curr, cnt + 1)
            ret.append(curr)
        
        return ret
            
            