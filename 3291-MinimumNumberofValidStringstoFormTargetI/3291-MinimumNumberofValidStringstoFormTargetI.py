# Last updated: 24/6/2025, 10:47:31 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y
inf = float('inf')

def getKMP(st):
    n = len(st)
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and st[i] != st[j]:
            j = lps[j - 1]
        if st[i] == st[j]:
            j += 1
            lps[i] = j
    
    return lps

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(words)
        m = len(target)

        matches = [0] * m

        for w, word in enumerate(words):
            lps = getKMP(word)
            j = 0
            for i in range(m):
                while j > 0 and target[i] != word[j]:
                    j = lps[j - 1]
                if target[i] == word[j]:
                    matches[i-j] = cmax(matches[i-j], j+1)
                    j += 1
                    if j == len(word): j = lps[j - 1]
    
        dp = [inf] * (m + 1)
        dp[0] = 0
        stack = deque([])
        for i in range(1, m+1):
            while stack and stack[0] < i:
                stack.popleft()
            
            if matches[i - 1]:
                index = i + matches[i - 1] - 1
                dp[index] = cmin(dp[index], dp[i-1] + 1)

                while stack and stack[-1] < index and dp[stack[-1]] > dp[index]:
                    stack.pop()
                
                if not stack or stack[-1] < index:
                    stack.append(index)
            
            if stack: dp[i] = min(dp[i], dp[stack[0]])

        return -1 if dp[m] == inf else dp[m]