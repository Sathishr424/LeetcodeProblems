# Last updated: 17/5/2025, 3:37:47 pm
class Solution:
    def maxSubstringLength(self, st: str, k: int) -> bool:
        if k == 0: return True
        n = len(st)

        start = [n] * 26
        end = [-1] * 26

        prefix = [[0] * 26 for _ in range(n+1)]
        
        for i, char in enumerate(st):
            char = ord(char) - 97
            if start[char] == n:
                start[char] = i
            end[char] = i

            for j in range(26):
                prefix[i+1][j] = prefix[i][j]
            
            prefix[i+1][char] += 1

        stack = []
        for char in range(26):
            if start[char] == n: continue

            s = start[char]
            e = end[char]

            for i in range(s+1, e):
                e = max(e, end[ord(st[i]) - 97])
                if e - s + 1 == n: continue
            
            heapq.heappush(stack, (e-s, s, e, char))
        
        visited = SortedList()

        while stack:
            dis, s, e, char = heapq.heappop(stack)
            index = visited.bisect_left(s)
            if index < len(visited) and visited[index] < e: continue

            if dis <= 1:
                k -= 1
                if k == 0: return True
                visited.add(s)
                continue

            if e-s+1 == n: continue

            left = prefix[s]
            right = prefix[e+1]

            match = True
            for i in range(26):
                cnt = right[i] - left[i]
                if cnt > 0 and (left[i] > 0 or prefix[-1][i] > cnt):
                    match = False
                    break
            
            if match:
                k -= 1
                if k == 0: return True
                visited.add(s)
    
        return False