# Last updated: 14/7/2025, 3:31:43 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        graph = defaultdict(list)
        half = n // 2

        freq = defaultdict(int)

        for char in label:
            freq[char] += 1

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(mask, x, st, index):
            if index == len(st): return True
            for y in graph[x]:
                if st[index] == label[y] and mask & (1 << y) == 0:
                    if dfs(mask | (1 << y), y, st, index + 1): return True
            return False
        
        def isMatch(st):
            # print(st)
            for i in range(n):
                if label[i] == st[0] and dfs(1 << i, i, st, 1):
                    return True
            return False
        
        max_size = 1
        def rec(st):
            nonlocal max_size
            new_st = st + st[::-1]
            is_pal = new_st == new_st[::-1]
            if is_pal and len(st) * 2 > max_size and isMatch(new_st):
                max_size = len(st) * 2
            for char in freq:
                if is_pal and freq[char] > 0 and len(st) * 2 + 1 > max_size and isMatch(st + char + st[::-1]):
                    max_size = len(st) * 2 + 1
                
                if freq[char] > 1:
                    freq[char] -= 2
                    rec(st + char)
                    freq[char] += 2
        
        rec('')
        return max_size
        