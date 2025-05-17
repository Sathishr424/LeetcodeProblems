# Last updated: 17/5/2025, 3:14:12 pm
class Solution:
    def maxSubstringLength(self, st: str, k: int) -> bool:
        if k == 0: return True
        n = len(st)

        uniq = defaultdict(int)
        start = defaultdict(int)
        end = defaultdict(int)

        prefix = [[0] * 26 for _ in range(n+1)]
        
        for i, char in enumerate(st):
            if char not in start:
                start[char] = i
            end[char] = i
            uniq[char] = 1

            for j in range(26):
                prefix[i+1][j] = prefix[i][j]
            prefix[i+1][ord(char) - 97] += 1


        stack = []
        for char in uniq:
            s = start[char]
            e = end[char]
            for i in range(s+1, e):
                e = max(e, end[st[i]])
            
            if e - s + 1 == n: continue
            heapq.heappush(stack, (e-s, s, e, char))
        
        visited = []


        while stack:
            dis, s, e, char = heapq.heappop(stack)
            # print(dis, s, e, char)
            index = bisect_left(visited, s)
            if index < len(visited) and visited[index] < e: continue

            if dis <= 1:
                # print(char, (s,e))
                # print(True)
                k -= 1
                if k == 0: return True
                visited.append(s)
                continue

            if e-s+1 == n: continue
            # print(char, (s,e))
            left = prefix[s]
            right = prefix[e+1]

            # print(left)
            # print(right)
            # print(prefix[-1])

            match = True
            for i in range(26):
                cnt = right[i] - left[i]
                if cnt == 0: continue
                if left[i] > 0:
                    match = False
                    break
                if prefix[-1][i] > cnt:
                    match = False
                    break
            # print(match, k)
            if match:
                k -= 1
                if k == 0: return True
                visited.append(s)
    
        return False