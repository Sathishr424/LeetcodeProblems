# Last updated: 12/6/2025, 5:53:51 am
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        counts = defaultdict(int)

        for char in t: counts[char] += 1
        
        tot = len(counts)
        
        stack = deque([])
        curr = defaultdict(int)
        matches = 0

        res = [-1, -1]

        for i in range(n):
            char = s[i]

            if char in counts:
                curr[char] += 1
                stack.append(i)

                if curr[char] == counts[char]:
                    matches += 1
                
                if matches == tot:
                    while True:
                        if res[0] == -1 or res[1] - res[0] > i - stack[0]:
                            res = [stack[0], i]
                        tmp = s[stack.popleft()]
                        curr[tmp] -= 1
                        if curr[tmp] < counts[tmp]: break
                    matches -= 1
        
        return '' if res[0] == -1 else s[res[0]:res[1]+1]