# Last updated: 17/5/2025, 3:42:22 pm
class Solution:
    def maxSubstringLength(self, st: str, k: int) -> bool:
        if k == 0: return True
        n = len(st)

        alp_to_index = [ord(a) - 97 for a in st]
        start = [n] * 26
        end = [-1] * 26

        prefix = [[0] * 26 for _ in range(n+1)]
        
        for i, char in enumerate(alp_to_index):
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
                e = max(e, end[alp_to_index[i]])

            if e - s + 1 == n: continue
            stack.append((e-s, s, e))
        
        stack.sort(key=lambda x: x[0])
        visited = SortedList()

        for dis, s, e in stack:
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