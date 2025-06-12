# Last updated: 12/6/2025, 5:48:18 am
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = {}

        for char in s1:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        n = len(s1)

        cnt = 0
        curr = defaultdict(deque)
        left = 0

        for i in range(len(s2)):
            char = s2[i]
            if char not in counts:
                cnt = 0
                left = i+1
                curr = defaultdict(deque)
            elif len(curr[char]) == counts[char]:
                index = curr[char].popleft()
                for j in range(left, index):
                    curr[s2[j]].popleft()
                
                curr[char].append(i)
                left = index+1
            else:
                curr[char].append(i)
                
                if i-left+1 == n: return True
        
        return False
